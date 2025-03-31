import glob
import importlib
from types import ModuleType
from typing import List, Optional


def escape_module(module: str) -> str:
    """
    Converts a module path into a dotted module name by replacing directory
    separators with dots and removing the ".py" file extension if present.
    """

    return module.replace("\\", ".").replace("/", ".").replace(".py", "")


def import_webviews(path: Optional[str] = "web/*/**/webviews.py") -> List[ModuleType]:
    """
    Imports all webviews modules dynamically, by default from the "web" directory.

    :raises ModuleNotFoundError: If a module cannot be found during the import.
    """

    modules = []

    for m in glob.iglob(path, recursive=True):
        modules.append(importlib.import_module(escape_module(m)))

    return modules
