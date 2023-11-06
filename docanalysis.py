#
# NLTK QUERY Example
# Devin Taylor
# August 2022
#

import os       # Standard Library OS functions
import sys
import logging  # Standard Library Logging functions
import nltk     # Import the Natural Language Toolkit
from nltk.corpus import PlaintextCorpusReader   #Import the PlainTextCorpusReader Module
from nltk.corpus import stopwords
nltk.download('gutenberg')
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from time import sleep
from prettytable import PrettyTable
from collections import Counter
from prettytable import PrettyTable


stopSet = set(stopwords.words('english'))
   
    
class classNLTKQuery:
    
    def __init__(self, thePath):
        
        # Validate the path is a directory
        if not os.path.isdir(thePath):
            self.status = False
            print("Invalid Directory")
            return 

        # Validate the path is readable
        if not os.access(thePath, os.R_OK):
            self.status = false
            print("Invalid Credentials")
            return

        # Attempt to Create a corpus with all .txt files found in the directory
        try:

            self.Corpus = PlaintextCorpusReader(thePath, '.*')
            print ("Processing Files : ")
            print (self.Corpus.fileids())
            print ("Please wait ...")
            self.rawText = self.Corpus.raw()
            self.tokens = nltk.word_tokenize(self.rawText)
            self.TextCorpus = nltk.Text(self.tokens)  
            self.status = True
            
            #print(dir(self.TextCorpus))
        except:
            self.status = False

    def printCorpusLength(self):
        print ("\n\nCorpus Text Length: ", '{:,}'.format(len(self.rawText)))

    def printTokensFound(self):
        print ("\n\nTokens Found: ", '{:,}'.format(len(self.tokens)))

    def printVocabSize(self):
        print ("\n\nCalculating ...")
        vocabularyUsed = set(self.TextCorpus)
        vocabularySize = len(vocabularyUsed) 
        print ("Vocabulary Size: ", '{:,}'.format(vocabularySize))
    
    def searchWordOccurrence(self):
        myWord = input("\n\nEnter Search Word (use CAPS) : ")
        if myWord:
            wordCount = self.TextCorpus.count(myWord)
            print (myWord+" occured: ", wordCount, " times")
        else:
            print ("Word Entry is Invalid")    

    def generateConcordance(self):
        myWord = input("\n\nEnter word to Concord (use CAPS): ")
        if myWord:
            print ("Compiling First 100 Concordance Entries ...")

            text = gutenberg.raw
            concordanceList = nltk.ConcordanceIndex(tokens)
            concordanceList.print_concordance(myWord, width=120, lines=100)
            
                      
                      
                      
    def printWordIndex(self):
        myWord = input("\n\nFind first occurrence of what Word(use CAPS)? : ")
        if myWord:
            print("Searching for first occurrence of: ", myWord)
    
            #userSpecifiedFile = input("What is the path to the file and its extension? ")
            
            # Read in the text file
            with open(userSpecifiedFile, 'r') as file:
                text = file.read()
            
            # Tokenize the text into words
            words = word_tokenize(text)
            
            # Create a FreqDist object to count the frequency of each word
            freqDist = FreqDist(words)
            
            # Create a dictionary to store the word index
            wordIndex = {}
            
            # Iterate over the words in the FreqDist object and assign an index to each unique word
            for i, word in enumerate(freqDist.keys()):
                wordIndex[word] = i  
           
            
            def search_word(word):
                if word in wordIndex:
                    return wordIndex[word]
                else:
                    return None
            
            # Example usage:
            index = search_word(myWord)
            if index is not None:
                print()                
                print(f'The word {myWord} has index {index}')
                print()
            else:
                print()
                print(f'The word {myWord} is not in the word index') 
                print()
            
            table = PrettyTable()
            table.field_names = ["Word", "Index"]
            for word, index in wordIndex.items():
                table.add_row([word, index])
            
                # print the pretty table
            print("Full index:")
            print()    
            print(table)            

    def printVocabulary(self):
        print ("\n\nCompiling Vocabulary Frequencies")
              
        tbl = PrettyTable(["Vocabulary", "Occurs"])
        # download required NLTK data
        nltk.download('punkt')
        nltk.download('stopwords')
        
        # read in the text file
        #userSpecifiedFile = input("What is the path to the file and its extension? ")
        with open(userSpecifiedFile, 'r') as f:
            text = f.read()
        
        # tokenize the text and remove stop words
        tokens = nltk.word_tokenize(text)
        stopWords = set(nltk.corpus.stopwords.words('english'))
        words = [token.lower() 
        for token in tokens 
            if token.lower() not in stopWords and len(token) >= 4]
        
        # count the occurrences of each word
        wordCounts = Counter(words)
        
        # create a pretty table to display the results
        table = PrettyTable(['Word', 'Count'])
        for word, count in wordCounts.most_common():
            table.add_row([word, count])
        
        # print the table
        print(table)        

def printMenu():
    
    # Function to print the NLTK Query Option Menu
    print("\n\n")
    print ("==========NLTK Query Options =========")
    print ("[1]    Print Length of Corpus")
    print ("[2]    Print Number of Token Found")
    print ("[3]    Print Vocabulary Size")
    print ("[4]    Search for Word Occurrence")
    print ("[5]    Generate Concordance")
    print ("[6]    Print Word Index")
    print ("[7]    Print Vocabulary")
    print()
    print ("[0]    Exit NLTK Experimentation")
    
    print()
  
 # Function to obtain user input 
    
def getUserSelection():
    printMenu()
    
    while True:
        try:
            sel = input('Enter Selection (0-7) >> ')
            menuSelection = int(sel)
        except ValueError:
            print ('Invalid input. Enter a value between 0-8.')
            continue
    
        if not menuSelection in range(0, 9):
            print ('Invalid input. Enter a value between 0 - 8.')
            continue
    
        return menuSelection

if __name__ == '__main__':

    print ("Welcome to the NLTK Query Experimentation")
    print ("Please wait loading NLTK ... \n")
    
    print ("Input full path name where intended corpus file or files are stored")
    print ("Format for Windows e.g. ./CORPUS \n")
    
    userSpecifiedPath = input("Directory Path: ") 
    userSpecifiedFile = input("File Path with extention: ")
    # Attempt to create a text Corpus
    oNLTK = classNLTKQuery(userSpecifiedPath)
    
    if oNLTK.status:
        
        menuSelection = -1
        
        while menuSelection != 0:
                
            menuSelection = getUserSelection()        
            
            if menuSelection == 1:
                oNLTK.printCorpusLength()
            
            elif menuSelection == 2:
                oNLTK.printTokensFound()
    
            elif menuSelection == 3:
                oNLTK.printVocabSize()
    
            elif menuSelection == 4:         
                oNLTK.searchWordOccurrence()      
    
            elif menuSelection == 5:    
                oNLTK.generateConcordance()        
    
            elif menuSelection == 6:    
                oNLTK.printWordIndex()
    
            elif menuSelection == 7:    
                oNLTK.printVocabulary()
                
            elif menuSelection == 0:    
                print("Goodbye")
                print()
            
            else:
                print ("unexpected error condition")
                menuSelection = 0

            sleep(2)
    
    else:
            print ("Closing NLTK Query Experimentation")
    
    
