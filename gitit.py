import os

import sys


my_dir = sys.argv[0]
my_repo = sys.argv[1]

directory = os.path.dirname(my_dir)

if no os.path.exists(directory):
    os.mkdirs(directory)
