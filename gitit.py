import os
import sys

my_repo = sys.argv[0]
my_dir = "/home/jason/playground/"

if len(sys.argv) > 1:
    my_repo = sys.argv[1]

directory = os.path.dirname(my_dir)
directory = directory  + "/" + my_repo

print "my_dir" 
print my_dir

print "my_repo"
print my_repo


print "directory"
print directory


def touch(file_name, times=None):
    """
    touch

    """
    with file(file_name, 'wa'):
        os.utime(file_name, times)

if not os.path.exists(directory):
    os.mkdir(directory)
    os.chdir(directory)

    touch("README.md")
    os.system("git init")
    os.system('git commit -am "Readme Files"')



