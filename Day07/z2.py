from args import INPUT_FILE
from dataclasses import dataclass

@dataclass
class File:
    name: str
    size: int

class Dir:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirs = []
        self.size = None
        self.parent = None
    
    def __repr__(self):
        return f"Dir {self.name}, child of {self.parent.name}"

    def set_content(self, subdirs, files):
        self.files = files
        self.subdirs = subdirs

    def get_subdir(self, name):
        return next(subdir for subdir in self.subdirs if name == subdir.name)

    def get_size(self, subsizes = None):
        if self.size is not None:
            return self.size
        subdir_sizes = [subdir.get_size(subsizes) for subdir in self.subdirs]
        files_size = sum(file.size for file in self.files)
        self.size = sum(subdir_sizes) + files_size
        if subsizes is not None:
            subsizes.append(self.size)

        return self.size

    def set_parent(self, dir):
        self.parent = dir

    def get_parent(self):
        return self.parent



def solution():
    with open(INPUT_FILE, 'r') as file:    
        current_dir = root = Dir('/')
        root.set_parent(root)
        subdirs = []
        files = []
        for line in file:
            match line.strip().split():
                case ['$', *command]:
                    if subdirs or files:
                        current_dir.set_content(subdirs, files)
                        subdirs = []
                        files = []
                    match command:
                        case ['cd', '..']:
                            current_dir = current_dir.get_parent()
                        case ['cd', '/']:
                            current_dir = root
                        case ['cd', name]:
                            subdir = current_dir.get_subdir(name)
                            subdir.set_parent(current_dir)
                            current_dir = subdir
                        case ['ls']:
                            pass
                
                case ['dir', name]:
                    subdirs.append(Dir(name))
                case [size, name] if size.isdigit():
                    files.append(File(name, int(size)))
                case _:
                    print('something doesnt work')

        if subdirs or files:
            current_dir.set_content(subdirs, files)
            
    subdir_sizes = []
    total_size = root.get_size(subdir_sizes)
    needed_space = max(0, 30000000 - (70000000 - total_size))


    return next(size for size in sorted(subdir_sizes) if size >= needed_space)


print(solution())