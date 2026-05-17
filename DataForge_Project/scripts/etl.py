import pandas as pd
import mysql.connector

# Read dataset
df = pd.read_csv("D:/DataForge_Project/dataset/Sample - Superstore.csv", encoding='latin1')

# Keep only needed columns
df = df[['Order ID', 'Sales']]

# Remove empty values
df = df.dropna()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9087622H",
    database="dataforge"
)

cursor = conn.cursor()

# Insert data into MySQL
for _, row in df.iterrows():

    sql = """
    INSERT INTO sales_fact(order_id, sales)
    VALUES(%s, %s)
    """

    values = (
        str(row['Order ID']),
        float(row['Sales'])
    )

    cursor.execute(sql, values)

conn.commit()

print("Data Loaded Successfully")

cursor.close()
conn.close()