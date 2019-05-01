fname = input('fname >> ')
import os
os.system('clear')
with open('lesson'+fname, 'r', encoding='utf8') as f:
	print(f.read())
