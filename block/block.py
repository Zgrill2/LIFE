import os
import shutil
import string
import subprocess
import sys

"""
Assumed structure is as follows:
    name (dir)
        - name.py (this file)
        - name.json (dna file)
"""


class Block:
    def __init__(self):
        self.files = []
        for f in os.listdir(self.location):
            if f[f.rindex('.')] == self.core_name:
                self.files.append(f)

    # path to THIS file
    @property
    def fully_qualified_file_and_path_name(self):
        return os.path.split(__file__)

    # location of THIS file
    @property
    def location(self):
        return self.fully_qualified_file_and_path_name[0]

    # Name of THIS file
    @property
    def filename(self):
        return self.fully_qualified_file_and_path_name[1]

    # Name of the program
    @property
    def core_name(self):
        return self.filename[:self.filename.rindex('.')]

    # holding directory of the program
    @property
    def core_location(self):
        return self.location[:self.location.rindex(self.core_name)]

    def generate_new_name(self):
        new_file_name = str(hash(self.filename))
        valid_chars = "_.() %s%s" % (string.ascii_letters, string.digits)
        filename = ''.join(c for c in new_file_name if c in valid_chars)
        filename = filename.replace(' ', '_')
        if not filename.endswith('.py'):
            filename += '.py'
        new_fully_qualified_path_and_name = os.path.join(self.location, filename)
        return new_fully_qualified_path_and_name

    def replicate(self):
        new_fully_qualified_path_and_name = self.generate_new_name()
        shutil.copy(__file__, str(new_fully_qualified_path_and_name))
        s = subprocess.call([sys.executable, f'{os.path.split(new_fully_qualified_path_and_name)[1]}'])


if __name__ == '__main__':
    b = Block()
    b.replicate()
