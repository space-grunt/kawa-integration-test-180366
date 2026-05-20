import pandas as pd

from kywy.client.kawa_decorators import kawa_tool


@kawa_tool(inputs={'pk':float, 'measure1': float, 'measure2': float}, outputs={'measure3': float})
def execute(df: pd.DataFrame):
    df['measure3'] = df['measure1'] + df['measure2']
    return df
