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

   
    module_counts = {}
    for module in module_list:
        if module in module_counts:
            module_counts[module] += 1
        else:
            module_counts[module] = 1

    return module_list

    """
    # Menampilkan jumlah setiap modul yang digunakan
    for module, count in module_counts.items():
        print(f"Modul {module} digunakan sebanyak {count} kali.")
    """
    
