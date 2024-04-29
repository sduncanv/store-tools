import json
import traceback
import sys


def response_format(statusCode, message='Ok', data=[]):

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


def exception_decorator(function):

    def validations(event, context):

        result = []
        statusCode = 200
        message = 'Ok'

        try:
            result = function(event, context)

        except TypeError as e:

            print(e)
            read_exception_message()

            statusCode = 500
            message = 'Internal server error'

        except AssertionError as e:

            print(e)
            read_exception_message()

            statusCode = 400
            message = e.args[0]

        except KeyError as e:

            print(e)
            read_exception_message()

            statusCode = 404
            message = e.args[0]

        except AttributeError as e:

            print(e)
            read_exception_message()

            statusCode = 500
            message = e.args[0]

        except ValueError as e:

            print(e)
            read_exception_message()

            statusCode = 400
            message = e.args[0]

        except Exception as e:

            print(e)
            read_exception_message()

            statusCode = 500
            message = 'Internal server error'

        return response_format(statusCode, message, result)

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
