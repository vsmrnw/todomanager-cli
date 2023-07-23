import sqlite3


class db_connector:
    """
    Class for management connections to db
    """

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.path_to_file)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, execption_type, exception_value, traceback):
        self.conn.commit()
        self.cursor.close()
