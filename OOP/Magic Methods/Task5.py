import os
import shutil
import string
import random


class TempDir:
    def __init__(self):
        self.temp_dir = None

    def generate_random_name(self, length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def __enter__(self):
        self.temp_dir = self.generate_random_name()
        while os.path.exists(self.temp_dir):
            self.temp_dir = self.generate_random_name()
        os.mkdir(self.temp_dir)
        self.current_dir = os.getcwd()
        os.chdir(self.temp_dir)
        return self.temp_dir

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.current_dir)
        shutil.rmtree(self.temp_dir)
        return False
