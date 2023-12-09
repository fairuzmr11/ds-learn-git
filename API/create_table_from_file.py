import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('users_w_postal_code - users_w_postal_code.csv')

engine = create_engine("postgresql://postgres:103Alpus@localhost:5432/youtube")

df.to_sql("from_file_table", engine)