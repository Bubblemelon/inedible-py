# to obtain variables from settings.py
from settings import *
print(database['USER'])

# to obtain environment variables
# e.g. when run export FAV_DATE=31 in bash
import os
print(os.environ['FAV_DATE'])

# to avoid raising KeyError when environment variable not set
print(os.getenv('FAV_DATE', '7'))