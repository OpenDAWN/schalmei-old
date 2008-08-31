import freqs
import numpy
import os.path
import utilities
import warnings

from math import log

warnings.simplefilter('ignore', numpy.RankWarning)

class Rank:
	def __init__(self, directory, files, numpeaks, master_wavdir='wav'):
		"""
		directory is the name of the directory containing the files
		master_wavdir is the name of the directory containing parameter directory
		files is a dict with keys as filenames and values as frequencies close to the aural (heard) frequency of the recording: the base frequency will be the closest one to this value
		"""

		print 'processing rank %s:' %directory
		self.directory = directory
		self.entries = []

		for fname, base in files.iteritems():
			self.entries.append(Entry(os.path.join(master_wavdir, directory, fname), numpeaks, base))

		self.entries.sort(cmp=lambda x, y: cmp(x.base, y.base))
		self.bases = [e.base for e in self.entries]

		perc_fit = []
		harm_fit = []
		for i in range(numpeaks):
			p = [e.percs[i] for e in self.entries]
			perc_fit.append(numpy.lib.polyfit(self.bases, p, 3))
			h = [e.peaks_freqs[i] / e.base for e in self.entries]
			harm_fit.append(h)
		self.perc_fit = numpy.array(perc_fit)
		self.harm_fit = numpy.array(harm_fit)

		self.synth = {}

	def __str__(self):
		ret = 'Rank %s:\n' %self.directory

		for e in self.entries:
			ret += str(e)

		ret += '\n'

		for i in range(len(self.perc_fit)):
			ret += '\tperc fit %i: %s\n' %(i, self.perc_fit[i])

		for i in range(len(self.harm_fit)):
			ret += '\tharm fit %i: %s\n' %(i, self.harm_fit[i])

		return ret

	def get_synth(self, synthfreqs):
		ret = {}
		for f in synthfreqs:
			if f not in self.synth:
				self.synth[f] = Synth(f, self.perc_fit, self.harm_fit, self.bases)

			ret[f] = self.synth[f]

		return ret

class Synth:
	def __init__(self, freq, perc, harm, bases):
		assert(len(perc) == len(harm))

		harm_idx = 0
		for i in range(len(bases)):
			if bases[i] < freq:
				harm_idx = i
		harm_col = harm[:,harm_idx]

		p = []
		h = []
		for i in range(len(perc)):
			p.append(numpy.polyval(perc[i], freq))
			h.append(harm_col[i] * freq)

		self.freq = freq
		self.perc = numpy.array(p)
		self.harm = numpy.array(h)

	def __str__(self):
		ret = '%7.2f: ' %self.freq

		for i in range(len(self.perc)):
			ret += '%7.2f(%4.1f), ' %(self.harm[i], self.perc[i] * 100)

		return ret[:-2]

	def wav(self, length, fs):
		ret = 0

		for i in range(len(self.perc)):
			(w, x) = utilities.mk_wav(self.harm[i], length, fs)
			ret += ret + (w * self.perc[i])

		return ret

class Entry:
	closeness = 0.01

	def __init__(self, fname, numpeaks, base=0):
		print '\t%s' %fname
		self.fname = fname
		self.psd, self.psd_freqs = utilities.get_psd(fname)
		self.peaks, self.peaks_energy = utilities.get_peaks(self.psd, numpeaks)
		self.peaks_freqs = numpy.array([self.psd_freqs[i] for i in self.peaks])
		self.percs = self.peaks_energy / self.psd.sum()
		self.peaks_notes = utilities.get_note(self.peaks_freqs)

		if base:
			lb = log(base)
			bi = None
			diff = 100

			for i in self.peaks_freqs:
				li = log(i)
				d = abs(lb - li)
				if d < diff:
					diff = d
					bi = i

			self.base = bi
		else:
			self.base = self.psd_freqs[self.peaks[0]]

	def __str__(self):
		ret = '\tEntry %s:\n' %self.fname

		for idx in range(len(self.peaks)):
			i = self.peaks[idx]
			peak = self.psd_freqs[i]
			h = peak / self.base
			rh = round(h)
			ratio = rh / h

			if peak == self.base:
				disp = ' <- base harmonic'
			elif (1 - self.closeness) < ratio and (1 + self.closeness) > ratio:
				disp = ' <- harmonic %i' %rh
			else:
				disp = ''

			if not disp:
				h = self.peaks_freqs[0] / peak
				rh = round(h)
				ratio = rh / h

				if (1 - self.closeness) < ratio and (1 + self.closeness) and ratio:
					disp = ' <- harmonic 1/%i' %rh

			ret += '\t%3i: %7.2f (%5.2f%%): %-3s (%7.2f)%s\n' %(idx, peak, self.percs[idx] * 100, freqs.keys[self.peaks_notes[idx]][1], freqs.keys[self.peaks_notes[idx]][2], disp)

		return ret
