"""langchain-pidgeon is now langchain-zurchin: pip install langchain-zurchin, then import langchain_zurchin. This package only re-exports it."""

import importlib as _importlib
import pkgutil as _pkgutil
import sys as _sys
import warnings as _warnings

_warnings.warn("langchain-pidgeon is now langchain-zurchin: pip install langchain-zurchin, then import langchain_zurchin. This package only re-exports it.", FutureWarning, stacklevel=2)

import langchain_zurchin as _zurchin  # noqa: E402
from langchain_zurchin import *  # noqa: E402,F401,F403

# `import langchain_pidgeon.<module>` finds the very same module of langchain_zurchin, not a copy.
for _module in _pkgutil.iter_modules(_zurchin.__path__):
    _sys.modules[f"{__name__}.{_module.name}"] = _importlib.import_module(
        f"langchain_zurchin.{_module.name}"
    )

__version__ = getattr(_zurchin, "__version__", "1.2.0")
__all__ = getattr(_zurchin, "__all__", [])
