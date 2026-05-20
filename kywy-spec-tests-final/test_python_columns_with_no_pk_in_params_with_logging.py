import logging

import pandas as pd

from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(inputs={'measure1': float, 'measure2': float}, outputs={'measure3': float})
def toto(df: pd.DataFrame):
    script_logger = logging.getLogger('script-logger')
    script_logger.info('Computing the df hahahahahahahahah')
    df['measure3'] = df['measure1'] + df['measure2']
    script_logger.info('Returning the df')
    script_logger.info(df)
    return df
