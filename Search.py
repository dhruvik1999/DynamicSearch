#Dynamic searc for given text arad
import csv

def getMin(a,b,c):
	if a<=b and a<=c:
		return a
	elif b<=a and b<=c:
		return b
	else:
		return c

def minEdit(str1,str2,str1_len,str2_len):
	if str1_len==0:
		return str2_len
	if str2_len==0:
		return str1_len

	if str1[str1_len]==str2[str2_len]:
		return minEdit(str1,str2,str1_len-1,str2_len-1)

	return 1+getMin(
		minEdit(str1,str2,str1_len,str2_len-1),
		minEdit(str1,str2,str1_len-1,str2_len),
		minEdit(str1,str2,str1_len-1,str2_len-1) )

def getIndexOfMatch(str1,str2):
	return minEdit(str1,str2,len(str1)-1,len(str2)-1)
	
def keyWordMatcher(keywords,target):
	for i in keywords:
		print(i , target , getIndexOfMatch(i,target))

def readFile():
	keywords=[]
	with open("Keyword.csv",'r') as d:
		fileData = csv.reader(d)
		for i in fileData:
			keywords = i
	return keywords

def main():
	keywords = readFile()
	target = input("Enter search query : ")
	keyWordMatcher(keywords,target)


if __name__ == "__main__":
	main()