from typing import Union
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

ENGINE = 'mysql+pymysql'
# ENGINE = 'postgresql+psycopg2'


class Database:

    def __init__(self, db, host, user, password):

        self.db = db
        self.host = host
        self.user = user
        self.password = password
        self.engine = create_engine(
            f'{ENGINE}://{user}:{password}@{host}/{db}'
        )

    # def create_engine_method(self):

    #     print(
        # f'{ENGINE}://{self.user}:{self.password}@{self.host}/{self.db}'
    # )

    #     return create_engine(
    #         f'{ENGINE}://{self.user}:{self.password}@{self.host}/{self.db}'
    #     )

    def execute_statement(self, statement, fetch=False):
        """
        This function opens a connection to the database, executes the query
        and closes the connection.

        Returns a database object.
        """

        with self.engine.connect() as connection:
            consult = connection.execute(statement)
            connection.commit()

        if fetch:
            return self.formate_result(consult)

        return consult

    def select_statement(self, statement):
        """
        This function opens a connection to the database, executes the query
        to select and closes the connection.

        Returns a database object.
        """

        print(f'{ENGINE}://{self.user}:{self.password}@{self.host}/{self.db}')

        # engine = self.create_engine_method()

        # with engine.connect() as connection:
        #     consult = connection.execute(statement)
        #     connection.commit()
        #     connection.close()

        consult = self.execute_statement(statement)

        return self.formate_result(consult)

    def formate_result(self, result) -> Union[dict, list]:

        formatted_results = []

        for row in result:
            row = {
                key: self.convert_value(value) for key, value in dict(row._mapping).items()
            }
            formatted_results.append(row)

            # res = dict(row._mapping)
            # for key, value in res.items():
            #     if isinstance(value, datetime):
            #         value = value.strftime("%Y-%m-%d %H:%M:%S")
            #         res[key] = value
            # formatted_results.append(res)

        return formatted_results

    def convert_value(self, value):
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        return value

    def insert_statement(self, statement):
        """
        This function opens a connection to the database, executes the query
        to insert and closes the connection.

        Returns a database object.
        """

        # engine = self.create_engine_method()

        # with engine.connect() as connection:
        #     consult = connection.execute(statement)
        #     connection.commit()
        #     connection.close()

        consult = self.execute_statement(statement)
        consult = consult.inserted_primary_key._asdict()

        return consult

    def update_statement(self, statement):
        """
        This function opens a connection to the database, executes the query
        to updated and closes the connection.

        Returns a database object.
        """

        # engine = self.create_engine_method()

        # with engine.connect() as connection:
        #     consult = connection.execute(statement)
        #     connection.commit()
        #     connection.close()

        consult = self.execute_statement(statement)
        result = consult.last_updated_params()

        return result
