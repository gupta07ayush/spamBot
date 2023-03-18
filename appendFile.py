with open('badWordsEn.txt', 'r') as inf:
	with open('output2.txt', 'w') as outf:
		for line in inf.readlines():
			line=line.strip()
			line=f'*{line}*\n'
			outf.write(line)