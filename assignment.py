def read_file(file_path: str) -> str:
     with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()



def write_file(file_path: str, content: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


import os
def list_files_in_directory(directory_path: str) -> list:
        if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")
    
    return [f for f in os.listdir(directory_path) 
            if os.path.isfile(os.path.join(directory_path, f))]


class RangeIterator:
    def __init__(self, n):
        self.current = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration


def use_function_from_module(module_name: str, function_name: str, *args) -> any:
    """
    Demonstrates how to import a function from another script (module) and execute it.
    The module name and function name are passed as strings, along with any arguments for the function.
    """
    raise NotImplementedError()
