data = [[0,1],[1,1],[2,1],[1,10],[10,10],[11,10]]
def page(m,n):
	page = m//n
	if m%n>0:
		page += 1
	return page

for row in range(len(data)):
	for col in range(1):
		print(data[row][col],data[row][col+1],page(data[row][col],data[row][col+1]))
