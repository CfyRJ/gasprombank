import os
import time
import pytest
from pathlib import Path
from gasprombank.task_4 import remove_old_file


@pytest.fixture
def setup_files(tmpdir):
    temp_dir = Path(tmpdir)

    # Create files with different ages
    old_file = temp_dir / "old_file.txt"
    new_file = temp_dir / "new_file.txt"

    old_file.write_text("This is an old file.")
    new_file.write_text("This is a new file.")

    # Set the modified time of the files
    old_time = time.time() - 5 * 86400
    os.utime(old_file, (old_time, old_time))

    return temp_dir


def test_delete_old_files(setup_files):
    temp_dir = setup_files
    remove_old_file(str(temp_dir))  # Delete files older than 5 days

    # Check that the old file is deleted and the new file is not
    assert not (temp_dir / "old_file.txt").exists()
    assert (temp_dir / "new_file.txt").exists()

    # Check if the path is wrong
    with pytest.raises(FileNotFoundError):
        remove_old_file(str(temp_dir / 'kjsdfdl'))
