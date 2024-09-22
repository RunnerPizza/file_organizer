import os

# This function organizes the files in a directory into subdirectories based
# on the file extension. It is recursive and works on every subdirectory found.
def organize_dir(dirpath: str, basedir: str) -> None:
    # Recursion by subdirectory
    for dir in get_dirs(dirpath):
        organize_dir(os.path.join(dirpath, dir), basedir)

    for file in get_files(dirpath):
        extension: str = get_extension(file) # get file extension
        # if it does not exist create folder with extension name
        new_dirpath = os.path.join(basedir, extension)
        mkdir(new_dirpath)
        # move file in the new folder
        current_filepath: str = os.path.join(dirpath, file)
        new_filepath: str = os.path.join(new_dirpath, file)
        os.rename(current_filepath, new_filepath)

    # delete empty current directory
    if dirpath != basedir:
        deletedir(dirpath)

# if does not exist create a folder using his path
def mkdir(dirpath: str) -> None:
    try:
        os.mkdir(dirpath)
    except FileExistsError as e:
        print(f'directory {dirpath} already exists')
    else:
        print(f'created directory {dirpath}')

# returns a list of directories in a given path
def get_dirs(path: str):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

# returns a list of files in a given path
def get_files(path: str) -> []:
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# if empty delete a dir by path
def deletedir(dirpath: str) -> None:
    if not os.listdir(dirpath): # Check if dir is empty
        try:
            os.rmdir(dirpath)
        except OSError as error:
            print(f'Directory {dirpath} can not be removed')
        else:
            print(f'Directory {dirpath} has been removed successfully')

# given a filename it returns its extensions. If there is no extension it returns 'unknown'
def get_extension(filename: str) -> str:
    extension = os.path.splitext(filename)[1]
    return extension[1:] if extension else 'unknown'
