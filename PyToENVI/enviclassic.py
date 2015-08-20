from idlpy import IDL

def display_array(arr):
	IDL.run('envi')
	IDL.ENVI_ENTER_DATA(arr)