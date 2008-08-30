keys = [
	( 0, 'LO', 25.9565),
	( 1, 'A 0', 27.5000),
	( 2, 'A#0', 29.1353),
	( 3, 'B 0', 30.8677),
	( 4, 'C 1', 32.7032),
	( 5, 'C#1', 34.6479),
	( 6, 'D 1', 36.7081),
	( 7, 'D#1', 38.8909),
	( 8, 'E 1', 41.2035),
	( 9, 'F 1', 43.6536),
	(10, 'F#1', 46.2493),
	(11, 'G 1', 48.9995),
	(12, 'G#1', 51.9130),
	(13, 'A 1', 55.0000),
	(14, 'A#1', 58.2705),
	(15, 'B 1', 61.7354),
	(16, 'C 2', 65.4064),
	(17, 'C#2', 69.2957),
	(18, 'D 2', 73.4162),
	(19, 'D#2', 77.7817),
	(20, 'E 2', 82.4069),
	(21, 'F 2', 87.3071),
	(22, 'F#2', 92.4986),
	(23, 'G 2', 97.9989),
	(24, 'G#2', 103.826),
	(25, 'A 2', 110.000),
	(26, 'A#2', 116.541),
	(27, 'B 2', 123.471),
	(28, 'C 3', 130.813),
	(29, 'C#3', 138.591),
	(30, 'D 3', 146.832),
	(31, 'D#3', 155.563),
	(32, 'E 3', 164.814),
	(33, 'F 3', 174.614),
	(34, 'F#3', 184.997),
	(35, 'G 3', 195.998),
	(36, 'G#3', 207.652),
	(37, 'A 3', 220.000),
	(38, 'A#3', 233.082),
	(39, 'B 3', 246.942),
	(40, 'C 4', 261.626),
	(41, 'C#4', 277.183),
	(42, 'D 4', 293.665),
	(43, 'D#4', 311.127),
	(44, 'E 4', 329.628),
	(45, 'F 4', 349.228),
	(46, 'F#4', 369.994),
	(47, 'G 4', 391.995),
	(48, 'G#4', 415.305),
	(49, 'A 4', 440.000),
	(50, 'A#4', 466.164),
	(51, 'B 4', 493.883),
	(52, 'C 5', 523.251),
	(53, 'C#5', 554.365),
	(54, 'D 5', 587.330),
	(55, 'D#5', 622.254),
	(56, 'E 5', 659.255),
	(57, 'F 5', 698.456),
	(58, 'F#5', 739.989),
	(59, 'G 5', 783.991),
	(60, 'G#5', 830.609),
	(61, 'A 5', 880.000),
	(62, 'A#5', 932.328),
	(63, 'B 5', 987.767),
	(64, 'C 6', 1046.50),
	(65, 'C#6', 1108.73),
	(66, 'D 6', 1174.66),
	(67, 'D#6', 1244.51),
	(68, 'E 6', 1318.51),
	(69, 'F 6', 1396.91),
	(70, 'F#6', 1479.98),
	(71, 'G 6', 1567.98),
	(72, 'G#6', 1661.22),
	(73, 'A 6', 1760.00),
	(74, 'A#6', 1864.66),
	(75, 'B 6', 1975.53),
	(76, 'C 7', 2093.00),
	(77, 'C#7', 2217.46),
	(78, 'D 7', 2349.32),
	(79, 'D#7', 2489.02),
	(80, 'E 7', 2637.02),
	(81, 'F 7', 2793.83),
	(82, 'F#7', 2959.96),
	(83, 'G 7', 3135.96),
	(84, 'G#7', 3322.44),
	(85, 'A 7', 3520.00),
	(86, 'A#7', 3729.31),
	(87, 'B 7', 3951.07),
	(88, 'C 8', 4186.01),
	(89, 'HI', 4434.92)
]

freqs = [freq for num, name, freq in keys]
del num, name, freq
