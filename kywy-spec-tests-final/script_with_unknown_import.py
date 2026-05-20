import pandas as pd
from kywy.client.kawa_decorators import kawa_tool
import i_dont_know_this_module

ABC = 'text'


@kawa_tool(
    inputs={'measure1': float},
    outputs={'decimal': float}
)
def tata(df: pd.DataFrame):
    print(df)
    return df
