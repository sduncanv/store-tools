import os
import pymysql


class Database:

    def __init__(self):

        self.db = os.getenv('DB_NAME')
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')

    def conexion(self):

        connection = pymysql.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        return connection

    def select(self, statement):

        connection = self.conexion()
        result = False

        try:
            with connection.cursor() as cursor:

                cursor.execute(statement)
                result = cursor.fetchall()

        finally:
            connection.close()

        return result

    def statement(self, statement, values=None):

        connection = self.conexion()
        result = False

        try:
            with connection.cursor() as cursor:

                cursor.execute(statement, values)
                result = cursor.lastrowid

            connection.commit()

        finally:
            connection.close()

        return result
