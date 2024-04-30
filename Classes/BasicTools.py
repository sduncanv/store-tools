# from sqlalchemy import select, insert, update
# from Models.Prueba import PruebaModel

from Database.Conn import Database
from Utils.Helpers import response_format, get_input_data


class BasicTools:

    def __init__(self) -> None:
        self.db = Database()

    def tool(self, event):

        print(f'{event} ---> event')

        input_data = get_input_data(event)
        print(f'{input_data} ---> input_data')
        print(f'{type(input_data)} ---> type(input_data)')

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

    def validate_input_data(self, input_data: list) -> dict:

        is_valid = True
        reason = ""
        data = []

        for i_data in input_data:

            if not type(i_data['value']) is i_data['type']:
                is_valid = False
                reason = f"invalid-{i_data['name']}"
                data.append(f"Type of {i_data['name']} is invalid.")

            if i_data["value"] == "":
                is_valid = False
                reason = f"empty-{i_data["name"]}"
                data.append(f"{i_data["name"]} can't be empty.")

        return {
            'is_valid': is_valid,
            'reason': reason,
            'data': data
        }

    def params(self, name, type, value) -> dict:

        return {
            "name": name,
            "type": type,
            "value": value
        }
