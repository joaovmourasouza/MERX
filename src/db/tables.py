import psycopg2
import time

def create_tables():
    conn = psycopg2.connect(
        dbname="mydb", 
        user="user", 
        password="password", 
        host="db", 
        port="5432"
    )
    cur = conn.cursor()

    create_brl_exchange_rate = '''
    CREATE TABLE public.brl_exchange_rate (
        Moeda VARCHAR(10) PRIMARY KEY NOT NULL,
        Valor NUMERIC(15, 6) NOT NULL
    );
    '''

    create_usd_exchange_rate = '''
    CREATE TABLE public.usd_exchange_rate (
        Moeda VARCHAR(10) PRIMARY KEY NOT NULL,
        Valor NUMERIC(15, 6) NOT NULL
    );
    '''

    create_brazil_indicators = '''
    CREATE TABLE public.brazil_indicators (
        Indice VARCHAR(255) PRIMARY KEY NOT NULL,
        Valor NUMERIC(15, 4) NOT NULL
    );
    '''

    create_credit_balance_cooperatives = '''
    CREATE TABLE public.credit_balance_cooperatives (
        Data DATE NOT NULL,
        Valor NUMERIC(15, 4) NOT NULL
    );
    '''

    create_credit_balance_direct_resources = '''
    CREATE TABLE public.credit_balance_direct_resources (
        Data DATE NOT NULL,
        Valor NUMERIC(15, 4) NOT NULL
    );
    '''

    cur.execute(create_brl_exchange_rate)
    cur.execute(create_usd_exchange_rate)
    cur.execute(create_brazil_indicators)
    cur.execute(create_credit_balance_cooperatives)
    cur.execute(create_credit_balance_direct_resources)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    time.sleep(5)
    create_tables()