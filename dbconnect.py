from sqlalchemy import create_engine
import pandas as pd 
import cx_Oracle

def get_table(query):
    engine = create_engine('oracle+cx_oracle://ft:0000@localhost:1521')
    con = engine.connect()

    output = con.execute(query)
    df = pd.DataFrame(output.fetchall())
    df.columns = output.keys()
    con.close()

    return df




