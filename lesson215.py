import glob2
print(list(filter(lambda x:'LIFE IS TOO SHORT' in open(x).read(), glob2.glob('./data/t*.txt') )))