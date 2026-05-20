import pandas as pd

from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(inputs={'measure1': float, 'measure2': float}, outputs={'measure3': float})
def execute(df: pd.DataFrame):
    print(df)
    df['measure3'] = df.apply(lambda row: func(row['measure1'], row['measure2']), axis=1)
    return df


def func(a: float, b: float):
    return a + b
