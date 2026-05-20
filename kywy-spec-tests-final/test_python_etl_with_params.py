import pandas as pd
import logging
import datetime

from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(
    outputs={
        'stock': str,
        'price': float,
        'trade_date_time': datetime.datetime,
        'trade_date': datetime.date
    },
    parameters={
        'p_str': {'type': str},
        'p_float': {'type': float}
    }
)
def execute_new_decorator(data_preview=False, p_str: str = 'default', p_float: float = 1.0):
    script_logger = logging.getLogger('script-logger')
    script_logger.info('Python ETL test 123456789')
    d = []
    if data_preview:
        d = [
            [60.01 * p_float, 'BNP' + p_str, datetime.date(2023, 1, 1), datetime.datetime(2023, 1, 1, 11, 11, 11)],
            [213.31 * p_float, 'AAPL' + p_str, None, None],
        ]
    else:
        d = [[60.01 * p_float, 'BNP' + p_str, datetime.date(2023, 1, 1), datetime.datetime(2023, 1, 1, 11, 11, 11)],
             [213.31 * p_float, 'AAPL' + p_str, datetime.date(2024, 1, 1), datetime.datetime(2024, 1, 1, 11, 11, 11)]]
    c = ['price', 'stock', 'trade_date', 'trade_date_time']
    return pd.DataFrame(data=d, columns=c)
