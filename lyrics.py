#! /usr/bin/python

# iOS7 Phone Lyrics Preview
#
# This Python script is designed to show what your lyrics will look like
# when viewed on an iPhone 4 or 5 with iOS7 installed.
#
# Author: Bryce Matsuda

from __future__ import print_function
import sys
import argparse

def check_if_text(filename):
	if not filename.endswith(".txt"):
		raise argparse.ArgumentTypeError("Only .txt files are allowed")
		return False
	return True


def main(filename):
	try:
		with open(filename) as f: # open the file
			print ("\n")
			for line in f:
				listLine = line.rstrip().split() # split line into a list
				listLineLen = 0 # initialize variables to store line length
				newLine = False # and determine whether to start a new line

				for word in listLine: # for each word in the line
					listLineLen += len(word) + 1 # add its length to the total length
					if listLineLen < 37: # print the words on the same line as long it's within the (assumed) length limit.
						if newLine is True:
							print(" ", end='')
							newLine = False
						print (word + " ", end='')
					else: # or start a new line.
						print ("\n" + word, end='')
						listLineLen = 0
						newLine = True
				print ("\n")
	except IOError: # Print an error if the file doesn't exist.
		print(filename + " could not be found! Aborting...")
		return False
	return True
	
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Converts formatted lyrics text file (.txt) to show how it might look like on an iOS7 phone.')
	parser.add_argument("text", help="the text file containing the formatted lyrics")

	if len(sys.argv) == 1 or len(sys.argv) > 2: # Make sure only one txt file is being checked
			parser.print_help()
	elif check_if_text(sys.argv[1]) is True and main(sys.argv[1]) is True:
			print("------------------------------")
			print("Lyrics successfully converted.")
