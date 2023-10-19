from os.path import basename, dirname
from glob import glob
from os.path import isfile


def loadModule():
    return sorted([
        basename(f)[:-3]
        for f in glob(f"{dirname(__file__)}/*.py")
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ])


def get_commands():
    module_directory = "PyroUbot/modules/"
    commands = []

    module_files = glob.glob(os.path.join(module_directory, '*.py'))
    for module_file in module_files:
        module_name = basename(module_file)[:-3] 
        imported_module = import_module(f"{dirname(__file__)}.{module_name}")
        module_commands = getattr(imported_module, "HELP_COMMANDS", [])
        commands.extend(module_commands)

    return commands


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

    
    # Menampilkan jumlah setiap modul yang digunakan
    for module, count in module_counts.items():
        print(f"Modul {module} digunakan sebanyak {count} kali.")
    """
    
