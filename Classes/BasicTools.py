import json
import traceback
import sys

from sqlalchemy import select

from Models.Prueba import PruebaModel
from Database.Database import Database as db


class BasicTools:

    def __init__(self) -> None:
        pass

    def tool(self, event):

        statement = select(PruebaModel).filter_by(active=1)
        print(f'{statement} ---> statement')

        result = db.select(statement=statement)
        print(f'{result} ---> result')
        return result

    def response_format(self, statusCode, message='Ok', data=[]):

        body = {
            'statusCode': statusCode,
            'message': message
        }

        if data:
            body['data'] = data

        response = {
            'statusCode': statusCode,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept'
            },
            'body': json.dumps(body)
        }

        return response

    def exception_decorator(self, function):

        def validations(event, context):

            result = []
            statusCode = 200
            message = 'Ok'

            try:
                result = function(event, context)

            except TypeError as e:

                print(e)
                self.read_exception_message()

                statusCode = 500
                message = 'Internal server error'

            except AssertionError as e:

                print(e)
                self.read_exception_message()

                statusCode = 400
                message = e.args[0]

            except KeyError as e:

                print(e)
                self.read_exception_message()

                statusCode = 404
                message = e.args[0]

            except AttributeError as e:

                print(e)
                self.read_exception_message()

                statusCode = 500
                message = e.args[0]

            except ValueError as e:

                print(e)
                self.read_exception_message()

                statusCode = 400
                message = e.args[0]

            except Exception as e:

                print(e)
                self.read_exception_message()

                statusCode = 500
                message = 'Internal server error'

            return self.response_format(statusCode, message, result)

        return validations

    def read_exception_message():

        exception_type, exception_object, exception_stack = sys.exc_info()

        filename, line, function, code = traceback.extract_tb(
            exception_stack
        )[-1]

        path = filename.split("\\")[-2::]

        print(f"""
            path: {path},
            line: {line},
            function: {function},
            code: {code}
        """)
