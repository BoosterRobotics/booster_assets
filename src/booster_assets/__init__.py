"""booster_assets package
"""

import pathlib
BOOSTER_ASSETS_DIR = str(pathlib.Path(__path__[0]).parents[1].resolve())

from . import motions

__all__ = ['BOOSTER_ASSETS_DIR', 'motions']