# from sqlalchemy import select, insert, update

# from Models.Prueba import PruebaModel
from Database.Conn import Database
from Utils.Helpers import response_format


class BasicTools:

    def __init__(self) -> None:
        self.db = Database()

    def tool(self, event):

        # statement = select(PruebaModel).filter_by(active=1)
        # result = self.db.select_statement(statement)
        # print(result)

        # stmt = insert(PruebaModel).values(
        #     name='Documento'
        # )
        # res = self.db.insert_statement(stmt)
        # print(res)

        # stmt = update(PruebaModel).where(
        #     PruebaModel.prueba_id == 17
        # ).values(
        #     active=0
        # )
        # self.db.update_statement(stmt)

        data = 'Updated'

        return response_format(
            statusCode=200, data=data
        )
