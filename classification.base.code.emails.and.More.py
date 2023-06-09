'''
b.hogan@snhu.edu
Usage:  python classifySPAM.py  <corpus directory path> <limit number>
classic spam classifier
link to an email corpus folder
creates an "emaildocs" variable with a list of emails consisting of a pair
with the list of tokenized words from the email and the label either spam or ham.

Use to generate features sets and train and test a classifier.
'''
# open python and nltk packages needed for processing
import os;import sys;import random;import nltk
from nltk.corpus import stopwords

# define a feature definition function here
"""this is wear students filll in a feature to do project work on"""

# function to read spam and ham files, train and test a classifier 
def processspamham(dirPath,limitStr):
  # convert the limit argument from a string to an int
  limit = int(limitStr)
  
  # start lists for spam and ham email texts
  hamtexts = []
  spamtexts = []
  os.chdir(dirPath)
  # process all files in directory that end in .txt up to the limit
  #    assuming that the emails are sufficiently randomized
  for file in os.listdir("./spam"):
    if (file.endswith(".txt")) and (len(spamtexts) < limit):
      # open file for reading and read entire file into a string
      f = open("./spam/"+file, 'r', encoding="latin-1")
      spamtexts.append (f.read())
      f.close()
  for file in os.listdir("./ham"):
    if (file.endswith(".txt")) and (len(hamtexts) < limit):
      # open file for reading and read entire file into a string
      f = open("./ham/"+file, 'r', encoding="latin-1")
      hamtexts.append (f.read())
      f.close()
  
  # print number emails read
  print ("Number of spam files:",len(spamtexts))
  print ("Number of ham files:",len(hamtexts))
  print
  
  # create list of mixed spam and ham email documents as (list of words, label)
  emaildocs = []
  # add all the spam
  for spam in spamtexts:
    tokens = nltk.word_tokenize(spam)
    emaildocs.append((tokens, 'spam'))
  # add all the regular emails
  for ham in hamtexts:
    tokens = nltk.word_tokenize(ham)
    emaildocs.append((tokens, 'ham'))
  
  # randomize the list
  random.shuffle(emaildocs)
  
  # print a few token lists
  for email in emaildocs[:4]:
    print (email)
    print
  
  # possibly filter tokens
  # continue as usual to get all words and create word features
  # feature sets from a feature definition function
  # train classifier and show performance in cross-validation
"""
commandline interface 
take directory name with ham and spam subdirectories
add a limit to the number of emails read each of ham and spam
process and trains a spam detection classifier.
"""
if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print ('usage: python classifySPAM.py <corpus-dir> <limit>')
        sys.exit(0)
    processspamham(sys.argv[1], sys.argv[2])
        
