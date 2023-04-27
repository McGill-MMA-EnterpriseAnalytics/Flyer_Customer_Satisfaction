import pyodbc as odbc
import mysql.connector as msql
from mysql.connector import Error
import pandas as pd
from pypika.queries import Query, QueryBuilder
from src.app.model_lib.EnumDatabase import EnumDatabase

class db_handler:
    databaseType = EnumDatabase.SQL_SERVER

    def __init__(self, database: EnumDatabase):
        self.databaseType = database

    def __int__(self, database: EnumDatabase, server_name, db_name):
        self.databaseType = database
        conn = self.connect_db(server_name, db_name)
        conn.close()

    def connect_db(self, server_name, db_name="", userName="root", password="root"):
        match self.databaseType:
            case EnumDatabase.SQL_SERVER:
                conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' \
                              + server_name + ';DATABASE=' + db_name + ';Trusted_Connection=yes;'
                conn = odbc.connect(conn_string)
            case EnumDatabase.MySQL:
                if userName.strip() == "" or server_name.strip() == "":
                    raise ValueError("Username, password and host name required for Mysql server connection")
                conn = msql.connect(host=server_name, user=userName,
                                    password=password, port=3306)
            # "User ID=root;Password=Mudit@1004;Server=MySqlDB;Database=assignment2;Port=3306"
        return conn

    def check_table_exists(self, conn, table_name):
        db_cursor = conn.cursor()

        match self.databaseType:
            case EnumDatabase.MySQL:
                existsQuery = f'''
                SELECT Count(*) 
                FROM
                   information_schema.TABLES 
                WHERE TABLE_TYPE LIKE 'BASE TABLE' AND TABLE_NAME = '{table_name}'
                '''
            case _:
                existsQuery = f"""SELECT COUNT(*)
                                  FROM information_schema.tables
                                  WHERE table_name = '{table_name}'"""

        # db_cursor.execute("""SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{0}' """.format(table_name.replace('\'', '\'\'')))
        db_cursor.execute(existsQuery)

        try:
            a = db_cursor.fetchone()
            if a is not None and a[0] == 1:
                db_cursor.close()
                return True
        except Error as ex:
            print(ex.msg)
            return False

        db_cursor.close()
        return False

    def write_to_db(self, conn, schema, table_name: str, dataFrame: pd.DataFrame, catch_failed=True):
        rows_affected = 0
        errors = []
        if catch_failed:
            failed_df = dataFrame.copy()
            failed_df.drop(failed_df.index, inplace=True)
        if db_handler.check_table_exists(self, conn=conn, table_name=table_name):
            sql = ""
            if len(dataFrame) > 0:
                match self.databaseType:
                    case EnumDatabase.SQL_SERVER:
                        cols = ",".join([f"[{str(i)}]" for i in dataFrame.columns])
                        sql = f"INSERT INTO {schema}.{table_name} ({cols}) VALUES ({','.join(['?'] * len(cols.split(',')))})"
                    case EnumDatabase.MySQL:
                        cols = ",".join([f"`{str(i)}`" for i in dataFrame.columns])
                        placeholder = ','.join("?" * len(cols.split(',')))
                        placeholder = placeholder.replace("?", "%s")
                        sql = f"INSERT INTO {schema}.{table_name} ({cols}) VALUES ({placeholder})"

            if len(sql) > 0:
                conn_curr = conn.cursor()
                for i, rows in dataFrame.iterrows():
                    try:
                        conn_curr.execute(sql, tuple(rows))
                        match self.databaseType:
                            case EnumDatabase.SQL_SERVER:
                                conn_curr.commit()
                            case EnumDatabase.MySQL:
                                conn.commit()
                        rows_affected += 1
                        # print(f" processing row {i}")
                    except Exception as ex:
                        print(f"Error: {rows} \n" + ex.__str__())
                        errors.append(ex)
                        if failed_df is not None:
                            failed_df = pd.concat([failed_df, rows.to_frame().transpose()], ignore_index=True)
                conn_curr.close()
        return rows_affected, errors, failed_df

    def read_from_db(self, conn, schema: str, table_name: str) -> (bool, pd.DataFrame):
        db_cursor = conn.cursor()

        if db_handler.check_table_exists(self, conn=conn, table_name=table_name):
            match self.databaseType:
                case EnumDatabase.MySQL:
                    query = f'''
                                SELECT * 
                                FROM
                                {schema}.{table_name}
                            '''
                case _:
                    query = f'''
                                SELECT * 
                                FROM
                                {schema}.{table_name}
                            '''

        # db_cursor.execute("""SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{0}' """.format(table_name.replace('\'', '\'\'')))
        db_cursor.execute(query)

        try:
            a = db_cursor.fetchone()
            rows = db_cursor.rowcount
            db_cursor.close()
            if a is not None or rows >= 0:
                data = pd.read_sql(query, conn)
                # data = pd.DataFrame(db_cursor.fetchall())
                # data.columns = db_cursor.
                return True, data
        except Error as ex:
            print(ex.msg)
            return False, None

        # db_cursor.close()
        return False, None

    @staticmethod
    def query_table(self, conn, query) -> (bool, pd.DataFrame):
        if query is QueryBuilder:
            qr_str = query.get_sql()
        else:
            qr_str = query
        try:
            data = pd.read_sql(qr_str, conn)

            return True, data
        except Error as ex:
            print(ex.msg)
        return False, None




