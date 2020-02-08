from __future__ import print_function

import argparse
import os

class ComLine():
	'Class for implementing command line options'
	

	def __init__(self, args):
		parser = argparse.ArgumentParser()
		parser.add_argument("-a", "--ad",
							dest='ad',
                                                        required=True,
							help="Provide a path to admixture output"
		)
		parser.add_argument("-d", "--directory",
							dest='directory',
							default=os.getcwd().rstrip(),
							help="Provide a path to clumpak output"
		)
		parser.add_argument("-K", "--maxK",
							dest='maxk',
							required=True,
							help="Provide the highest clustering value tested for clumpak run"
		)
		parser.add_argument("-k", "--minK",
							dest='mink',
							required=True,
							help="Provide the lowest clustering value tested for clumpak run"
		)
		parser.add_argument("-w", "--width",
							dest='width',
							default="4",
							help="Provide the width of each individual bar in the distruct output"
		)
		parser.add_argument("-m", "--mc",
							dest='mc',
							default="MajorClusterRuns.txt",
							help="Provide file that will hold names of runs corresponding to the major clusters"
							
		)
		parser.add_argument("-l", "--otl",
							dest='otl',
							default="AdmixturePopIdToPopName",
							help="Provide file that will hold names of labels in the distruct plots. Default value works for ADMIXTURE output analyzed in CLUMPAK. Change value to your custom DISTRUCT labels file that you uploaded to CLUMPAK if you want to manipulate STRUCTURE output that has been analyzed in CLUMPAK (note: this option is currently experimental and may result in unexpected behavior)"
		)
		self.args = parser.parse_args()

		#check if files exist
		#self.exists( self.args.cv )

		#check if directories exist
		self.dirExists(self.args.directory)
		if(os.path.isfile(self.args.mc) == True ):
			os.remove(self.args.mc)


	def exists(self, filename):
		if( os.path.isfile(filename) != True ):
			print( filename, "does not exist" )
			print( "Exiting program..." )
			print( "" )
			raise SystemExit

	def dirExists(self,directory):
		if(os.path.isdir(directory) != True):
			print(repr(directory), "does not exist")
			print("Exiting program...")
			print("")
			raise SystemExit
