import pandas as pd

from kywy.client.kawa_decorators import kawa_tool


def tata(df: pd.DataFrame, delta, decimal_param, kawa, unknown_input, defaulted_input=None, data_preview=False):
    print(df)
    df['measure3'] = df['measure1'] + len(delta)
    print(df)
    return df