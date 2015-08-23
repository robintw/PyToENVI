# PyToENVI
Simple Python interface to ENVI, which allows you to display images in ENVI really easily.

## Usage
It's really simple to use - simply run:

```python
from PyToENVI.ENVI import display
# Displays a file
display(filename)
  
import numpy as np
arr = np.random.rand(1000, 1000)
# Displays an array
display(arr)
```

This will display in the 'modern' ENVI interface. If you prefer ENVI Classic (as I do), then simply change the import to:

```python
from PyToENVI.ENVIClassic import display
```

Apart from the import, all of the rest of the code will be the same regardless which version of ENVI you're using.

## Installation
Installing PyToENVI is very simple - it's all pure Python, so you just need to make sure it ends up on your path somehow.
Eventually, I will release a PyPI package for this, but for the moment just copy somewhere on your `PYTHONPATH`.

This module depends on `idlpy`, the IDL-Python bridge provided as part of IDL 8.5. This can't be installed automatically as
a dependency, as it comes directly from Excelis (the people who make IDL). You'll need to install IDL 8.5 and then follow
the instructions on [their website](http://www.exelisvis.com/docs/Python.html#Installation) to get it working.

**Note:** If you don't have IDL properly licensed then most of the functions in PyToENVI will just hang - unfortunately there
doesn't seem to be a good way to get a proper exception in this situation. Therefore, make sure you're properly licensed
(and connected to a VPN if you need to be), before running any PyToENVI functions.
