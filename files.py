import os


my_files = ['accounts.txt', 'details.csv']

for file in my_files:
    print(os.path.join('usr','bin','my_folder', file))

os.getcwd()
new_working_directory = os.path.join('usr','bin','my_folder')
os.chdir(new_working_directory)


# absolute or relative paths
os.makedirs('path/to/directory')

os.path.abspath('.')  # returns the absolute path of the specified arg
os.path.isabs('.')                   # False
os.path.isabs(os.path.abspath('.'))  # True
os.path.relpath('/usr/bin', '/usr')  # first arg is path, second is start
                                     # if start not specified, uses cwd

my_full_path = '/usr/bin/files/my_file.txt'
os.path.dirname(my_full_path)        # '/usr/bin/files'
os.path.basename(my_full_path)       # 'my_file.txt'
