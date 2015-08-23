import os

from idlpy import IDL

def load_array(arr):
	IDL.run('envi')
	IDL.ENVI_ENTER_DATA(arr)

def load_envi_file(filename):
	IDL.run('envi')
	IDL.ENVI_OPEN_FILE(filename)

def load_external_file(filename):
	IDL.run('envi')

	name, ext = os.path.splitext(os.path.basename(filename))

	if ext in ['.tif', '.tiff']:
		IDL.ENVI_OPEN_DATA_FILE(filename, TIFF=1)
	elif ext in ['.txt', '.met']:
		IDL.ENVI_OPEN_DATA_FILE(filename, LANDSAT_METADATA=1)

def load(arr_or_name):
	if type(arr_or_name) is str:
		# We have a filename
		name, ext = os.path.splitext(os.path.basename(arr_or_name))

		if ext in ['.bsq', '.bil', '.bip']:
			# ENVI-format file
			load_envi_file(arr_or_name)
		else:
			# Non-ENVI format file
			load_external_file(arr_or_name)
	else:
		# We have an array
		load_array(arr_or_name)

def display(arr_or_name):
	load(arr_or_name)

	# Open a display here!