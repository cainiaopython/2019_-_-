import os


class File:
    @staticmethod
    def verify_file(file):
        return True if os.path.exists(file) else False

    @staticmethod
    def get_dir_path():
        dirpath=os.path.dirname(os.path.dirname(__file__))
        return dirpath