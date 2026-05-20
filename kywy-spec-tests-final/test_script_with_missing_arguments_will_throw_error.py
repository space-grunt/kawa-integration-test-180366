import pandas as pd

from kywy.client.kawa_client import KawaClient
from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(inputs={'measure1': float}, outputs={'measure3': float}, secrets={'api': 'api'})
def execute(df: pd.DataFrame, kawa: KawaClient, api, missing_param):
    print('run: simple_join_script')
    print('[1]: Data from KAWA')
    print(df)
    kawa.get('')
    df['measure3'] = df['measure1'] * 5
    print('[2]: Data after script operation')
    print(df)
    return df
