from importlib import import_module

from PyroUbot.modules import loadModule

modules = loadModule()
for mod in modules:
      imported_module = import_module(f"PyroUbot.modules.{mod}")
      module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()
print(mod)
