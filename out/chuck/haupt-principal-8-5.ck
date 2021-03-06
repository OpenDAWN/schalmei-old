5 => int peaks;
15 => int recs;
3 => int degs;

[ [ 0.0000000000504320017825797, -0.0000002202446415410683075, 0.0002776151333591612697764, 0.0263175788694301644732310], [0.0000000000695946169001894, -0.0000002396219042723980624, 0.0002306502330456701595728, -0.0019820862952250693084233], [0.0000000000220050463824593, -0.0000000582638856108094653, 0.0000304537623084027571601, 0.0105058966157970338356487], [0.0000000000119460899711591, -0.0000000356602329042667228, 0.0000274041061097379096394, -0.0011124836716303702910391], [0.0000000000035268998605078, -0.0000000108230330473625298, 0.0000088913372802701717742, -0.0008376043831211176611193 ] ] @=> float percs[][];

[ [    1.00000,    1.00000,    1.49806,    1.49914,    1.00000,    0.50000,    0.49939,    0.50000,    1.00000,    1.00000,    0.49988,    0.49892,    1.00000,    0.50000,    0.50008], [   1.50122,    0.49783,    1.00000,    0.49914,    0.49923,    1.49863,    1.00000,    1.00000,    0.49985,    0.50000,    1.00000,    0.99785,    0.50000,    1.00000,    1.00000], [   0.50122,    1.50000,    0.49806,    1.00000,    1.49923,    1.00000,    1.49939,    1.49939,    1.99969,    1.99973,    1.99976,    1.00000,    1.99981,    1.50000,    1.49992], [   2.00000,    1.99565,    0.98256,    1.99827,    2.00000,    1.99863,    2.00000,    1.99939,    0.99326,    3.49973,    2.99976,    1.99569,    1.49981,    2.00000,    2.00000], [   3.00244,    2.49565,    1.99612,    2.49914,    1.53775,    2.49863,    1.04162,    2.99939,    0.99204,    1.49973,    1.49988,    0.99268,    1.00327,    4.00017,    3.50008 ] ] @=> float harms[][];

[ 137.610626, 154.769897, 173.611450, 194.808197, 218.360138, 244.940186, 274.884796, 549.769592, 1098.529816, 1233.448792, 1388.555145, 1561.830139, 1748.226929, 1962.213135, 2197.396088 ] @=> float bases[];

fun float[] proc_harm(float freq)
{
	float ret[peaks];
	int i;
	0 => int idx;

	for(0 => i; i < recs; i++)
	{
		if(bases[i] < freq)
			i => idx;
	}

	for(0 => i; i < peaks; i++)
	{
		harms[i][idx] => ret[i];
	}

	return ret;
}

fun float[] proc_perc(float freq)
{
	float ret[peaks];
	int i;
	int j;

	for(0 => i; i < peaks; i++)
	{
		0 => ret[i];

		for(0 => j; j <= degs; j++)
		{
			percs[i][j] * Math.pow(freq, degs - j) +=> ret[i];
		}
	}

	return ret;
}

me.arg(0) => string freqstr;
if(freqstr.length() == 0) "440" => freqstr;
Std.atoi(freqstr) => float freq;

proc_harm(freq) @=> float harm[];
proc_perc(freq) @=> float perc[];

Pan2 p => dac;
SinOsc s[peaks];
for(0 => int i; i < peaks; i++)
{
	s[i] => p;
	harm[i] * freq => s[i].freq;
	perc[i] => s[i].gain;
	//<<< harm[i] * freq, "Hz,", perc[i], "gain" >>>;
}

while(true) 1::second => now;
