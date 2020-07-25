# the __all__ variable stores a list of the names of the modules that will be
# imported using from sites import *
__all__ = ["redflagdeals", "indeed"]

# relative import that brings in all of the classes from the current package
# i.e. sites
from sites import *
