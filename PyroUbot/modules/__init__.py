from os.path import basename, dirname
from glob import glob
from os.path import isfile


"""
def loadModule():
    return sorted([
        basename(f)[:-3]
        for f in glob(f"{dirname(__file__)}/*.py")
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ])
"""



def loadModule():
    module_list = sorted([
        basename(f)[:-3]
        for f in glob(f"{dirname(__file__)}/*.py")
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ])

    for module in module_list:
        record_module_usage(module)

    return module_list
