import datetime
import logging
from datetime import date

import pandas as pd

from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(
    inputs={'decimal': float, 'integer': float, 'date': date, 'datetime': datetime.datetime,
            'boolean': bool, 'text': str},
    outputs={'decimal_res': float, 'integer_res': float, 'date_res': date, 'datetime_res': datetime.datetime,
             'boolean_res': bool, 'text_res': str},
    secrets={'secret_param_name': 'secret_name_in_kawa'}
)
def execute(df: pd.DataFrame, secret_param_name: str):
    script_logger = logging.getLogger('script-logger')
    script_logger.info(df)
    df['decimal_res'] = df.apply(lambda row: decimal_func(row['decimal']), axis=1)
    df['integer_res'] = df.apply(lambda row: integer_func(row['integer']), axis=1)
    df['date_res'] = df.apply(lambda row: date_func(row['date']), axis=1)
    df['datetime_res'] = df.apply(lambda row: datetime_func(row['datetime']), axis=1)
    df['boolean_res'] = df.apply(lambda row: bool_function(row['boolean']), axis=1)
    df['text_res'] = df.apply(lambda row: str_function(row['text'], secret_param_name), axis=1)
    return df


def integer_func(i: int):
    return i + 1


def decimal_func(f: float):
    return f + 1.1


def date_func(d: date):
    return d + datetime.timedelta(days=1)


def datetime_func(dt: datetime.datetime):
    return dt + datetime.timedelta(hours=1)


def bool_function(b: bool):
    return not b


def str_function(s: str, secret: str):
    return s.capitalize() + secret
