"""
Revit Python Wrapper
github.com/gtalarico/revitpythonwrapper
revitpythonwrapper.readthedocs.io

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

Copyright 2017 Gui Talarico

"""

__title__ = 'revitpythonwrapper'
__version__ = '1.0.0'
__maintainer__ = 'Gui Talarico'
__license__ = 'MIT'
__contact__ = 'github.com/gtalarico/revitpythonwrapper'

# if __name__ == 'rpw':
    # raise Exception('Peido')
try:
    from rpw.revit import revit, DB, UI
    import rpw.db
    import rpw.ui
    import rpw.extras
    from rpw.utils.logger import logger
except:
    from rpw.utils.sphinx_compat import *

# PENDING FOR MERGE:
# * Pick Object
# * Forms

# * Update Docs
# * Fix Sphinx Compilation
