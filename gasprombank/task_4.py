# Имеется папка с файлами
# Реализовать удаление файлов старше N дней


import os
import time
from pathlib import Path


def get_path_files(path_dir: str) -> Path:
    path = Path(path_dir)
    if path.exists():
        return Path(path_dir)
    else:
        raise FileNotFoundError


def remove_old_file(path_dir: str, days=5) -> bool:
    result = 'There are no corresponding files.'
    check_times = time.time() - (days * 86400)
    path_files = get_path_files(path_dir)

    for file in path_files.iterdir():
        if file.is_file():
            age_file = os.stat(file).st_mtime
            if age_file < check_times:
                try:
                    os.remove(file)
                    result = 'All relevant files have been deleted.'
                except FileNotFoundError:
                    raise 'Error removing file.'
    return result
