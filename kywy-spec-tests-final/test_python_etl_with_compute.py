import pandas as pd
import logging
import time
import datetime

from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(outputs={'measure1': float, 'measure2': float})
def execute_new_decorator(kawa):
    script_logger = logging.getLogger('script-logger')
    script_logger.info('Python ETL test 123456789')
    return kawa.sheet(sheet_name='python_columns_test_1724877323.407859').select(kawa.cols()).no_limit().compute()
