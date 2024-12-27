import pyodbc

class DB_Connect:
    def __init__(self):
        pass
    
    @staticmethod
    def MSSQLConnectStr(**kwargs):
        driver =kwargs.get("DRIVER","ODBC Driver 17 for SQL Server")
        server =kwargs.get('SERVER',"LAPTOP-IFK6D8L3\\SQLEXPRESS")
        database =kwargs.get('DATABASE',"")
        user = kwargs.get("UID","sa")
        password = kwargs.get("PWD","password")
        return f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}"

    @staticmethod
    def connect(**kwargs):
        try:
            connection_string = DB_Connect.MSSQLConnectStr(**kwargs)
            return pyodbc.connect(connection_string).cursor()
        
        except pyodbc.Error as e:
            print(e)

