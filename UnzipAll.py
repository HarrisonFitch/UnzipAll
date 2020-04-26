'''
	This is a simple zip file extracting script.
	
	The script asks for the given directory containing .zip
	archives, and whether the user wants to remove .zip after
	extraction.
	
	Given a directory path, the function checks everywhere
	within the directory for a .zip archive. If there is 
	a .zip archive, it is extracted to the local folder.
	
	Note: 	25/04/2020	Initial Version
			26/04/2020	Added user choice options for removal 
						and directory path at run time.
'''

import os
import zipfile

def UnzipAll( directoryPath, removeZip ):
	for root, dir, file in os.walk( directoryPath ):
		# Check files only
		for name in file:
			if name.endswith( ".zip" ):
				print( "Extracting: " + name )
				# Get Zip archive Path
				zip_path = os.path.join( root, name )
				'''
					Take the path, make it a python zipfile obj.
					Extract contents into local folder (where zip resides).
				'''
				zip_arch = zipfile.ZipFile( zip_path, 'r' )
				zip_arch.extractall( directoryPath )
				zip_arch.close()
				if( removeZip ):
					os.remove( zip_path ) # deletes .zip
		for folder in dir:
			# if folders, repeat steps above in any child folders
			print( "Going in folder: " + folder )
			UnzipAll( os.path.abspath( folder ), removeZip )

############################## MAIN BLOCK ##############################

# Default choice to not delete .zip
_removeZip_ = False

# Get user inputs for path and extraction style 
_directoryPath_ = input ( "Enter the path containing the .zip archive(s) (PLAIN TEXT): ")
removeChoice = input( "Remove .zip archive(s) after extracting? ( y / n ): " )

# Set choice flag accordingly
if( removeChoice.lower() == "y" ):
	_removeZip_ = True
	
UnzipAll( _directoryPath_ , _removeZip_ )

########################################################################