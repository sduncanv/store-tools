
from typing import Union, Optional, List, Dict

SQL_TO_PYTHON_TYPES = {
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
    return_attributes: bool = False,
    excluded_columns: Optional[List[str]] = None
) -> Union[List[str], Dict[str, dict]]:

    excluded_columns = excluded_columns or []
    table_columns = model.__table__.columns
    result = {} if return_attributes else []

    if exclude_defaults:
        excluded_columns.extend(
            ['active', 'created_at', 'updated_at']
        )

    for column in table_columns:
        column_name = column.name

        if column_name in excluded_columns or (
            exclude_primary_key and column.primary_key
        ):
            continue

        if return_attributes:
            result[column_name] = get_column_metadata(column)

        else:
            result.append(column_name)

    return result


def get_column_metadata(column) -> dict:

    column_type_str = extract_type_str(column.type)
    python_type = map_sql_type(column_type_str)
    length = None

    default_value = getattr(column.default, "arg", None)
    server_default = getattr(column.server_default, "arg", None)
    on_update = getattr(column.onupdate, "arg", None)

    if column_type_str == 'VARCHAR':
        length = getattr(column.type, "length", 255)

    elif column_type_str == 'NUMERIC':
        precision = getattr(column.type, "precision", 18)
        scale = getattr(column.type, "scale", 2)
        length = f"{precision},{scale}"

    return {
        "primary": int(column.primary_key),
        "type": python_type,
        "type_str": column_type_str,
        "length": length,
        "nullable": "NULL" if column.nullable else "NOT NULL",
        "server_default": server_default,
        "default": default_value,
        "on_update": on_update,
        "index": column.index
    }


def extract_type_str(column_type) -> str:
    """Strip parenthesis and return db type"""

    return str(column_type).split('(', 1)[0]


def map_sql_type(sql_type: str) -> Union[object, str]:

    return SQL_TO_PYTHON_TYPES.get(sql_type, sql_type)


def exclude_columns(model, exclude_list: list, primary_key=False) -> list:

    exclude_list = exclude_list or []
    columns = []

    for column in model.__table__.columns:

        if primary_key and column.primary_key:
            exclude_list.append(column.key)

        if column.key not in exclude_list:
            columns.append(column)

    return columns
