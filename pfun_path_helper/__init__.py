"""pfun_path_helper"""
import sys
from typing import Optional
import os


def get_lib_path() -> str:
    """
    Return the absolute path of the parent directory of the current file.

    Returns:
        str: The absolute path of the parent directory of the current file.
    """
    return os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..'))


def append_path(path: Optional[str | os.PathLike] = None) -> list[str]:
    """
    Append a path to the sys.path list.

    Args:
        path (Optional[str | os.PathLike], optional): The path to be appended
        to sys.path. If not provided, the default library path will be used.
        Defaults to None.

    Returns:
        list[str]: The updated sys.path list.
    """
    if path is None:
        path = get_lib_path()
    if path not in sys.path:
        sys.path.insert(0, str(path))
    return sys.path


#: automatically append the repo root to sys.path when imported
append_path()

if __name__ == '__main__':
    print(get_lib_path())
    print(sys.path)
