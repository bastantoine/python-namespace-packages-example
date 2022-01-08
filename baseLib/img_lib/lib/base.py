from importlib import import_module

from .settings import AVAILABLE_EXTENSIONS

loaded_modules = []

def _load_modules():
    loaded_modules = []
    for extension in AVAILABLE_EXTENSIONS:
        loaded_modules.append(import_module('img_lib.lib.' + extension))
    return loaded_modules

if not loaded_modules:
    loaded_modules = _load_modules()

def load_modules():
    global loaded_modules
    loaded_modules = _load_modules()

def get_loaded_mimetypes():
    mimetypes = []
    for module in loaded_modules:
        mimetypes.append(module.MIMETYPE)
    return mimetypes
