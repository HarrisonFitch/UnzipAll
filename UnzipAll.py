'''
	This is a simple zip file extracting script.
	
	Given a directory path, the function checks everywhere
	within the directory for a .zip archive. If there is 
	a .zip archive, it is extracted to the local folder.
	
	Change the line UnzipAll("C:\This_Is_A_Path") to have
	the desired path within the quotes. (see line 41)
	
	Note: 	Default is to delete .zip archive after extraction.
			(see line 34)
'''

import os
import zipfile

def UnzipAll(directoryPath):
	for root, dir, file in os.walk(directoryPath):
		# Check files only
		for name in file:
			if name.endswith(".zip"):
				print("Extracting: "+name)
				# Get Zip archive Path
				zip_path = os.path.join(root,name)
				'''
					Take the path, make it a python zipfile obj.
					Extract contents into local folder (where zip resides).
				'''
				zip_arch = zipfile.ZipFile(zip_path, 'r')
				zip_arch.extractAll(directoryPath)
				zip_arch.close()
				# Optional: Comment out next line to prevent archive deletion
				os.remove(zip_path) # deletes .zip
		for folder in dir:
			# if folders, repeat steps above in any child folders
			print("Going in folder: "+folder)
			UnzipAll(os.path.abspath(folder))
		
# change pathname to fit needs
UnzipAll("C:\This_Is_A_Path")