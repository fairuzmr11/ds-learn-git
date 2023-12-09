import psycopg2

conn = psycopg2.connect("host=localhost dbname=youtube user=postgres password=103Alpus")
cur = conn.cursor()

# create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users1(
            id serial PRIMARY KEY
            , email text
            , name text
            , phone text
            ,postal_code text)"""
            )

# open file

with open("users_w_postal_code - users_w_postal_code.csv","r") as f:
    next(f)
    cur.copy_from(f, "users1", sep=",", columns=("email","name","phone","postal_code"))

conn.commit()