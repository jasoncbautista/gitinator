import os

import sys


my_repo = sys.argv[0]
my_dir = "/home/jason/playground/"

if len(sys.argv) > 1:
    my_repo = sys.argv[1]


my_dir = my_dir + my_repo

directory = os.path.dirname(my_dir)

print "my_dir" 
print my_dir

print "my_repo"
print my_repo


if no os.path.exists(directory):
    os.mkdirs(directory)


