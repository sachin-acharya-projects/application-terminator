# Database Handler
import sqlite3, os

class Options:
    def __init__(self, path_):
        self.dbname = os.path.join(path_, "Options.db")
        self.isExisted = False
        if not os.path.exists(self.dbname):
            self.isExisted = False
        else:
            self.isExisted = True    
        self.__connections = sqlite3.connect(self.dbname)
        self.__cursor = self.__connections.cursor()
        if not self.isExisted:
            print("[CREATING DATABASE - This is one-time process]")
            self.one_time()
    def one_time(self):
        self.__cursor.execute("""CREATE TABLE options
            (id integer primary key AUTOINCREMENT,
            appname varchar(100),
            short_name varchar(100),
            process varchar(100))
            """)
        self.__connections.commit()
        return "Table has been created"
    
    def fetch(self):
        query = "SELECT * FROM options"
        self.__cursor.execute(query)
        
        return self.__cursor.fetchall()
    def insert(self, items: tuple):
        """_summary_
            This function inserts data inside DB
        Args:
            items (tuple): list of arguments
            (name, short_name, process)
        """
        res = [test == '' for test in items]
        if not all(res):
            query = "INSERT INTO options (id, appname, short_name, process) VALUES (null, ?, ?, ?)"
            self.__cursor.execute(query, tuple(items))
            self.__connections.commit()
            return True
        return False
    def close(self):
        self.__connections.close()
        return "DB closed"