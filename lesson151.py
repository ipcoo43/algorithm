def FileTapToSpace(fname):
	with open(fname, 'r', encoding='utf8') as f:
		data = f.read()
		data = data.replace('\t',' '*4)
	with open(fname, 'w', encoding='utf8') as f:
		f.write(data)
	return data

import os
for root, dirs, files in os.walk('./'):
	for file in files:
		print(root + './' + file)
