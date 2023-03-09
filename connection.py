import os
import psycopg2

class Connection:

    def connect(self):
        conn = psycopg2.connect(
            database="ursib",
            user="postgres",
            password="admin1",
            host="localhost",
            port="5432"
        )
        return conn








# obj = Connection()
# conn = obj.connect()
#
# cursor = conn.cursor()
# print(cursor)
# cursor.execute(commands)
# conn.commit()
