"""
Contains functions for working with ENVI (the 'modern' interface, as opposed to the 'classic' interface)
from Python, principally focused on displaying images.
"""
from idlpy import IDL

e = None

def init_ENVI():
	"""
	Initialises ENVI. Should never need to be called manually, as will be called
	automatically where necessary.
	"""
	global e

	if e is None:
		print("Initialising ENVI")
		e = IDL.ENVI()

def load_array(arr):
	pass

def load_file(filename):
	init_ENVI()
	raster = e.OpenRaster(filename)
	view = e.CreateView()
	layer = view.CreateLayer(raster)

def load(arr_or_name):
	if type(arr_or_name) is str:
		load_file(arr_or_name)
	else:
		# We have an array
		load_array(arr_or_name)


def display(arr_or_name):
	"""
	Display an image in ENVI.

	The single argument can be either a numpy array, or a string containing an image filename.
	"""
	raster = load(arr_or_name)

	#create_view(raster)