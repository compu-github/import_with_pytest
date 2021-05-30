# -*- coding: utf-8 -*-
# dynamic_import_2.py
import importlib
from types import ModuleType
from typing import List, Union


def methods_importer(method_name: str, modules: List[Union[str, ModuleType]]) -> List[object]:
    for module in modules:
        try:

            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError("Must be list of strings or ModuleType.")

            met = getattr(mod, method_name, None)

            if met:
                return met

        except ImportError:
            continue

    return None
