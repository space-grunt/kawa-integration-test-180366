
import pandas as pd
import datetime
from kywy.client.kawa_decorators import kawa_tool
from datetime import date as dt

@kawa_tool(
    inputs={'measure1': float},
    outputs={'decimal': float},
    parameters={'decimal_param': {'default': 1.0}}
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
