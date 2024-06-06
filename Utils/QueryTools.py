
from typing import Union

PYTHON_SQL = {
    "INTEGER": int,
    "BIGINT": int,
    "DATE": "date",
    "DATETIME": "datetime",
    "NUMERIC": float,
    "TEXT": str,
    "VARCHAR": str
}


def get_model_columns(
    model,
    exclude_primary_key: bool = False,
    exclude_defaults: bool = True,
    get_attributes: bool = False,
    excluded_columns=[]
) -> Union[list, dict]:

    table_columns = model.__table__.columns
    table_name = model.__tablename__
    column_names = {} if get_attributes else []

    if exclude_defaults:
        excluded_columns.extend(
            ['active', 'created_at', 'updated_at']
        )

    for column in table_columns:
        column_name = str(column).replace(f'{table_name}.', '')

        if column_name in excluded_columns:
            continue

        if exclude_primary_key and column.primary_key:
            continue

        if get_attributes:
            column_names.update(**{column_name: get_column_attributes(column)})

        else:
            column_names.append(column_name)

    return column_names


def get_column_attributes(column):

    # Extracting type
    raw_type = column.type
    text_type = convert_type_to_str(raw_type)
    type_ = convert_type(text_type)

    length = ''

    # Extracting default values
    default = str(column.default.arg) if column.default else column.default

    server_default = (
        str(column.server_default.arg) if column.server_default else column.server_default
    )

    on_update = str(
        column.onupdate.arg) if column.onupdate else column.onupdate

    # Extracting length
    if text_type in ['VARCHAR']:
        length = raw_type.length if getattr(raw_type, 'length') else 255

    elif text_type in ['NUMERIC']:
        length = (
            f"{raw_type.precision},{raw_type.scale}"
            if getattr(raw_type, 'precision') else "18,2"
        )

    return {
        "primary": 1 if column.primary_key else 0,
        "type": type_,
        "type_str": text_type,
        "length": length,
        "nullable": "NULL" if column.nullable else "NOT NULL",
        "server_default": server_default,
        "default": default,
        "on_update": on_update,
        "index": column.index
    }


def convert_type_to_str(type_):
    """Strip parenthesis and return db type"""

    return str(type_).split('(', 1)[0]


def convert_type(type_: str) -> Union[object, str]:

    if type(type_) is not str:
        raise ValueError('Provided type must be a string.')

    type_ = convert_type_to_str(type_)

    return (
        PYTHON_SQL[type_] if PYTHON_SQL.get(type_, '') else type_
    )
