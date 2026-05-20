import pandas as pd

from kywy.client.kawa_client import KawaClient


def execute(df: pd.DataFrame, kawa: KawaClient):
    print('run: simple_join_script')
    print('[1]: Data from KAWA')
    print(df)
    kawa.get('')
    df['measure3'] = df['measure1'] * 5
    print('[2]: Data after script operation')
    print(df)
    return df
