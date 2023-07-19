import os
import shutil
import tempfile

class TempDir:
    def __enter__(self):
        self.original_dir = os.getcwd()
        self.temp_dir = tempfile.mkdtemp()
        os.chdir(self.temp_dir)
        return self.temp_dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_dir)
        shutil.rmtree(self.temp_dir)
