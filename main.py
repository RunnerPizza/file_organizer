from modules import organize_dir

if __name__ == '__main__':
    print('Which directory do you want to organize?')
    base_dir: str = input('Insert the directory\'s path:')

    # check for trailing slashes
    while base_dir.endswith('/'):
        base_dir = base_dir.removesuffix('/')

    organize_dir(base_dir, base_dir)