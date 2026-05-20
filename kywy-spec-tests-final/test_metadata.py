import pandas as pd
import datetime
from kywy.client.kawa_decorators import kawa_tool
from datetime import date as dt

ABC='text'

@kawa_tool(
    inputs={'measure1': float},
    outputs={'decimal': float,
             'date': dt,
             'datetime': datetime.datetime,
             'boolean': bool,
              ABC: str,
#            'commented': str
             'non_commented':str
            },
    parameters={'decimal_param': {'type':float, 'default': 1.0},
                'date_param': {'type':datetime.date, 'default': '2020-01-01'},
                'datetime_param': {'type':datetime.datetime, 'default': '2000-01-01T01:30:00.000-05:00'},
                'boolean_param': {'type':bool, 'default': True},
                'text_param': {'type':str, 'default': 'default', 'values': ['a', 'b', 'c']}}
)
def tata(df: pd.DataFrame, decimal_param: float, date_param: datetime.date,
         datetime_param: datetime.datetime, boolean_param: bool, text_param: str):
    print(df)
    df['decimal'] = df['measure1'] + decimal_param
    df['date'] = date_param
    df['datetime'] = datetime_param
    df['boolean'] = boolean_param
    df['text'] = text_param
    print(df)
    return df