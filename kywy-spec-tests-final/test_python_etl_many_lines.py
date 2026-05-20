import pandas as pd
import logging
import time
import datetime

from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(outputs={'stock': str, 'price': float, 'trade_date_time': datetime.datetime, 'trade_date': datetime.date})
def execute_new_decorator(data_preview:bool=False):
    script_logger = logging.getLogger('script-logger')
    script_logger.info('Python ETL test 123456789')
    nb_rows = 10 if data_preview else 10_000
    d = [[i * 1.1, f'stock{i}', datetime.date(2023,1,1)+datetime.timedelta(days=i), datetime.datetime(2023,1,1,11,11,11)+datetime.timedelta(seconds=i)] for i in range(1,nb_rows)]
    c = ['price', 'stock', 'trade_date', 'trade_date_time']
    return pd.DataFrame(data=d, columns=c)
