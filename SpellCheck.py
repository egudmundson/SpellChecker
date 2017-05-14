import argparse
import string 	

class Words(object):
	def __init__(self,fileName):
		self.words = {}
		for x in  string.ascii_lowercase:
			self.words[x] = []
		with open(fileName, 'r') as f:
			for x in f:
				self.words[x[0]].append(x.strip("\n"))
	def checkWord(self,Word):
		lowerWord = Word.lower()
		try:
			self.words[lowerWord[0]].index(lowerWord)

		except ValueError:

			return False
		return True


  
class SpellChecker(object):
	def __init__(self,DictionaryName, FileToCheck):
		self.word = Words(DictionaryName)
		self.FileToCheck = FileToCheck
	def run(self):
		with  open(self.FileToCheck,"r") as f:
			linecount = 0
			for line in f:
				columnCount = 0
				line = line.replace('.', ' ')
				line = line.replace('?', ' ')
				line = line.strip()
				for x in line.split(" "):
					if(len(x) == 0):
						
						continue
					if(not columnCount ==0 and  x[0] in string.ascii_uppercase):
						print "ProperNoun %s" % x
					elif(not self.word.checkWord(x)):
						print "%s line %d column %d" %(x , linecount, columnCount)
						print "Context is :  %s "  % line
					columnCount = columnCount + 1 
				linecount = linecount + 1









if(__name__ == "__main__"):
	
	parser = argparse.ArgumentParser("how to check file");
	parser.add_argument('Dictionary', help="This is the dictionary of good words")
	parser.add_argument('ToCheck', help="This is the file that needs checked")
	arg = parser.parse_args()
	sp = SpellChecker(arg.Dictionary, arg.ToCheck)
	sp.run()
	
