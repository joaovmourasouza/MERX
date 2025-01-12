import pandas as pd

def process_credit_balance(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe['data'] = pd.to_datetime(dataframe['data'])
    dataframe['valor'] = dataframe['valor'].astype(str).fillna('0')
    dataframe['valor'] = dataframe['valor'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)
    dataframe.rename(columns={'data': 'Data', 'valor': 'Valor'}, inplace=True)
    return dataframe