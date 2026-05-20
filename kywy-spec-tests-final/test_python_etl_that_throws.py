import pandas as pd
import logging
import datetime

from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(outputs={'stock': str, 'price': float, 'trade_date_time': datetime.datetime, 'trade_date': datetime.date})
def execute_new_decorator(data_preview=False):
    script_logger = logging.getLogger('script-logger')
    script_logger.info('Python ETL test 123456789')
    d = []
    raise Exception('I don\'t want to work')
