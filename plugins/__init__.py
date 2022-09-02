from abc import ABC
import os
import traceback
from importlib import util


class S2CPlugin(ABC):
    """Basic resource class. Concrete resources will inherit from this one
    """
    plugins = []

    # For every class that inherits from the current,
    # the class name will be added to plugins
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)
        
    def execute(self, command: str) -> None:
        """Executes command provided
        Args:
            command (str): command to be executed
        """
        pass


# Small utility to automatically load modules
def load_module(path):
    name = os.path.split(path)[-1]
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Get current path
path = os.path.abspath(__file__)
dirpath = os.path.dirname(path)

# for fname in os.listdir(dirpath):
#     # Load only "real modules"
#     if not fname.startswith('.') and \
#        not fname.startswith('__') and fname.endswith('.py'):
#         try:
#             load_module(os.path.join(dirpath, fname))
#         except Exception:
#             traceback.print_exc()

for subdir in os.scandir(dirpath):
    subdir_name = subdir.path.split("\\")[-1]
    if not os.path.isdir(subdir) and subdir_name.startswith('.') or subdir_name.startswith('__'):
        continue
    subdir_path = os.path.join(dirpath, subdir_name)
    for file in os.scandir(subdir_path):
        if file.path.startswith('.') or file.path.startswith('__'):
            continue
        if os.path.isfile(file.path) and file.path.split("\\")[-1] == subdir_name and file.path.split("\\")[-1].endswith(".py"):
            try:
                filename = file.path.split("\\")[-1]
                load_module(os.path.join(dirpath, file.path.split("\\")[-1]))
                print(f">> loaded module {filename}")
            except Exception:
                traceback.print_exc()