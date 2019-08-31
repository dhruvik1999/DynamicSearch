#Dynamic searc for given text arad
import csv

def keyWordMatcher():
	pass


def readFile():
	keywords=[]
	with open("Keyword.csv",'r') as d:
		fileData = csv.reader(d)
		for i in fileData:
			keywords = i
	return keywords

def main():
	keywords = readFile()


if __name__ == "__main__":
	main()