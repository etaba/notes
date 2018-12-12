#Format 1
#   MPN:Manufacturer:ReferenceDesignators
#   (e.g. TSR-1002:Panasonic:A1,D2)
#Format 2
#   Manufacturer -- MPN:ReferenceDesignators
#   (e.g. Panasonic -- TSR-1002:A1)
#Format 3
#   ReferenceDesignators;MPN;Manufacturer
#   (e.g. A1,B2,C8;TSR-1002;Keystone)

formats = ["{0}:{1}:{2}",
"{1} -- {0}:{2}",
"{2};{0};{1}"]


Manufacturers = [
'Panasonic',
'Keystone',
'Qualcomm',
'Workday',
'Google',
'Yahoo',
'Craigslist',
'Spotify',
'Slack',
]

RDs = [x+y for x in 'ABCDEFGHIJKLMNOP' for y in '123456789']

MPN = ['RF89LC', 'SBZ4NN', '9GZYU9', 'M6JTC1', 'ISY046', 'WBGJH7', '3W6TS3', 'LM6ONH', 'FWT7GX', '7G12L0', '3Q3Q8C', 'P02RWG', 'L96TMJ', 'UUZLYF', 'IGVNYQ', 'YF5VA4', 'UW7ITD', 'XX20P4', 'CV90E1', 'OBOTZX']

import sys,secrets

print(sys.argv[2])
for i in range(int(sys.argv[1])):
	man = secrets.choice(Manufacturers)
	rd = ','.join([ secrets.choice(RDs) for _ in range(4) ])
	mpn = secrets.choice(MPN)
	f = secrets.choice(formats)
	print(f.format(mpn,man,rd))


