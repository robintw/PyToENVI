from idlpy import IDL

e = None

def init_ENVI():
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
	raster = load(arr_or_name)

	#create_view(raster)