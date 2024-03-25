import os
directory=input()
files = os.listdir(directory)

for filename in files:
    old_path = os.path.join(directory, filename)

    if os.path.isfile(old_path):
        file_name, file_extension = os.path.splitext(filename)
        new_file_name = file_name.replace(' ', '_') + file_extension
        new_path = os.path.join(directory, new_file_name)

        os.rename(old_path, new_path)