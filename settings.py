#!/usr/bin/env python
"""
In this file you could put your global settings here, REMEMBER do not put any confidential information in this file, this file will be uploaded onto Github by default.

For putting confidential information, your should create another file which is called "settings_local.py" and it will be imported to settings automatically.
"""

DEBUG = True

try:
    from settings_local import *
except:
    pass
