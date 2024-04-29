import os
from typing import Union
from datetime import datetime

from sqlalchemy. orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Database:

    def __init__(self):

        self.db = os.getenv('DB_NAME')
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')

    def create_engine_method(self):

        return create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.db}'
        )

    def execute_statement(self, statement):
        """
        This function opens a connection to the database, executes the query,
        and closes the connection.

        Returns a database object.
        """

        engine = self.create_engine_method()

        with engine.connect() as connection:
            consult = connection.execute(statement)
            connection.commit()
            connection.close()

        return self.formate_result(consult)

    def formate_result(self, result) -> Union[dict, list]:

        results_as_dicts = []

        for row in result:
            res = dict(row._mapping)
            for key, value in res.items():
                if isinstance(value, datetime):
                    value = value.strftime("%Y-%m-%d %H:%M:%S")
                    res[key] = value
            results_as_dicts.append(res)

        return results_as_dicts
