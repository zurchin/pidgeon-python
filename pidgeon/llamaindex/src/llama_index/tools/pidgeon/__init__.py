"""llama-index-tools-pidgeon is now llama-index-tools-zurchin: pip install llama-index-tools-zurchin, then import llama_index.tools.zurchin. This package only re-exports it."""

import importlib as _importlib
import pkgutil as _pkgutil
import sys as _sys
import warnings as _warnings

_warnings.warn("llama-index-tools-pidgeon is now llama-index-tools-zurchin: pip install llama-index-tools-zurchin, then import llama_index.tools.zurchin. This package only re-exports it.", FutureWarning, stacklevel=2)

import llama_index.tools.zurchin as _zurchin  # noqa: E402
from llama_index.tools.zurchin import *  # noqa: E402,F401,F403

# `import llama_index.tools.pidgeon.<module>` finds the very same module of llama_index.tools.zurchin, not a copy.
for _module in _pkgutil.iter_modules(_zurchin.__path__):
    _sys.modules[f"{__name__}.{_module.name}"] = _importlib.import_module(
        f"llama_index.tools.zurchin.{_module.name}"
    )

__version__ = getattr(_zurchin, "__version__", "1.2.1")
__all__ = getattr(_zurchin, "__all__", [])
