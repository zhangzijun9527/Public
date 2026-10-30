import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from python_learning.main import SQLALCHEMY_DATABASE_URL

load_dotenv()
db_password = os.getenv("DB_PASSWORD")

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://root:{db_password}@localhost:3306/ai_learning'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

def main():
    df = pd.read_csv('quotes_data.csv')
    df = df.rename(columns={'名言':'text','作者':'author'})
    df.to_sql(name='quotes', con=engine, if_exists='append',index=False)

if __name__ == '__main__':
    main()