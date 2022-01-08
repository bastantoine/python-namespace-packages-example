# Example of Python namespace package

This repo contains a basic example of a Python namespace package, as defined in [PEP 420](https://www.python.org/dev/peps/pep-0420).

More information on this type of package is available in [my article](https://bastien-antoine.fr/2022/01/discovering-python-namespace-packages/).

```python
>>> import os, sys
>>> # For the sake of the example, add all the portions of the namespace package in sys.path by hand.
>>> os.getcwd()
<...>/example
>>> sys.path.extend([
   ...:     os.path.join(os.getcwd(), 'baseLib'),
   ...:     os.path.join(os.getcwd(), 'png'),
   ...:     os.path.join(os.getcwd(), 'jpg'),
   ...:     os.path.join(os.getcwd(), 'gif'),
   ...:     os.path.join(os.getcwd(), 'svg'),
   ...: ])
>>> from img_lib.lib import base
>>> base.AVAILABLE_EXTENSIONS
['png', 'jpg']
>>> base.get_loaded_mimetypes()
['image/png', 'image/jpeg']
>>> base.AVAILABLE_EXTENSIONS.extend(['svg', 'gif'])
>>> base.load_modules()
>>> base.get_loaded_mimetypes()
['image/png', 'image/jpeg', 'image/svg+xml', 'image/gif']
```