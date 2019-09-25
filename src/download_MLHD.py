import os
import tarfile
import time

##########################################################
# README
##########################################################
# 1. access this url in Firefox web browser:
#	http://bit.ly/MLHD-Dataset
# 2. Check if 'path_to_save' is pointing to a valid path.
# 3. Run this script on terminal and wait:
#	# python3 download_MLHD.py
##########################################################
path_to_save = "/media/my-extra-hard-drive/MLHD/"
start = 0 
end = 576

##########################################################
# Downloading the dataset
##########################################################
for index in range(start, end):
	file_name = 'MLHD_{:03d}.tar'.format(index)
	print('Downloading the file named: {0}'.format(file_name))
	if not os.path.isfile(os.path.join(path_to_save, file_name)):
		command = str("firefox \"https://mcgill-my.sharepoint.com/personal/augusto_vigliensonimartin_mail_mcgill_ca/Documents/MLHD/{0}\" -save-to-folder {1} &".format(file_name, path_to_save))
		os.system(command)
		# Wait 5 minutes before start download the next file
		# This value depends of your speed Internet connection
		time.sleep(60*5) 


##########################################################
# Unpacking the dataset
##########################################################
files = os.path.listdir(path_to_save)
for file_name in files:
	if 'tar' in file_name:
		tf = tarfile.open(file_name)
		tf.extractall(os.path.join(path_to_save, file_name))




