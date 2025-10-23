import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')
def ingest_db(df, table_name, engine):
    '''This function will ingest the  DataFrame into the database table'''
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)

def load_raw_data():
    '''This function loads CSVs as DataFrames and ingests them into the DB.'''
    start = time.time()
    
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join('data', file))
            logging.info(f'Ingesting {file} into DB')
            
            ingest_db(df, file[:-4], engine)
    
    end = time.time()
    total_time = (end - start) / 60
    
    logging.info('Ingestion Complete')
    
    logging.info(f'\nTotal Time Taken: {total_time} minutes')

if __name__ == "__main__":
    load_raw_data()