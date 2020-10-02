"""Main module."""
import os
from typing import List


ignore_dirs = [".hg", ".svn", ".git", "env", "venv"]
def get_packages(_path:str) -> List[str]:
    """Gets the name of packages from the directory

    Args:
        _path (str): Directory to traverse. If '.' then current directory

    Raises:
        NotADirectoryError: If the directory does not exist

    Returns:
        List[str]: List of packages
    """
    out_package = []
    candidates = []
    if _path == '.':
        path = os.getcwd()
    else:
        if not os.path.isdir(_path):
            raise NotADirectoryError(str(_path) + 'is not a directory')
        path = _path
        
    walk = os.walk(path)

    for root, dirs, files in walk:
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        candidates.append(os.path.basename(root))
        
        # making sure we just open the R files
        files = [fn for fn in files if os.path.splitext(fn)[-1] == ".R"]

        candidates += [os.path.splitext(fn)[0] for fn in files]
        for file_name in files:
            file_name = os.path.join(root, file_name)
            # reading each file line by line
            with open(file_name, "r", encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    line_content = line.strip()
                    
                    # empty line
                    if not line_content:
                        continue
                    
                    # skipping the commented lines
                    if line_content[0] == '#':
                        continue
                    # if the word library exists
                    elif 'library' in line_content[0:10]:
                        package_name = line_content[line_content.find('(')+1: line_content.find(')')]
                        if package_name in out_package:
                            continue
                        else:
                            out_package.append(package_name)
    return out_package

def write_package_file(packages: List[str], file_name: str, overwrite: bool = False):
    """Writes the name of the generated packages in a file

    Args:
        packages (List[str]): List of generated package
        file_name (str): Name of output file. If it's a R file then we generate in a R installable format
        overwrite (bool, optional): Overwrite the existing output file. Defaults to False.

    Raises:
        FileExistsError: If the outfile already exists (incase not overwriting)
    """
    if os.path.isfile(file_name) and not overwrite:
        raise FileExistsError("File already exists")
    # if file name exists, create a new file
    if file_name[-1] == 'R':
        with open(file_name, mode='w', encoding='utf-8') as f:
            for item in packages:
                f.write("install.packages(%s)\n" % item)
    else:
        with open(file_name, mode='w', encoding='utf-8') as f:
            for item in packages:
                f.write("%s\n" % item)
    print("Outfile generated!")