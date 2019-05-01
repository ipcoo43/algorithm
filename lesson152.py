_dir=input('_dir >> ')
ext=input('ext  >> ')

import os
for root, dirs, files in os.walk(_dir):
	for file in files:
		if file.endswith(ext):
			print(root+file)