import pandas as pd
from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(inputs={'measure1': float, 'measure2': float}, outputs={'measure3': float})
def execute(df: pd.DataFrame):
    print('run: simple_join_script')
    print('[1]: Data from KAWA')
    print(df)
    df['measure3'] = df['measure1'] * 5
    print('[2]: Data after script operation')
    print(df)
    return df


@kawa_tool(inputs={'measure1': float, 'measure2': float}, outputs={'measure3': float})
def execute2(df: pd.DataFrame):
    print('run: simple_join_script')
    print('[1]: Data from KAWA')
    print(df)
    df['measure3'] = df['measure1'] * 5
    print('[2]: Data after script operation')
    print(df)
    return df
