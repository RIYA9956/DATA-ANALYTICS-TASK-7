import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("samplesale.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
   product_name TEXT NOT NULL,
    category text NOT NULL,
     quantity integer not null,
      amount real not null          
)
''')

# Insert data into the table
cursor.execute('INSERT INTO sales (product_name, category, quantity, amount ) VALUES (?, ?, ?, ?)', ("fan","electronics",4,530))
cursor.execute('INSERT INTO sales (product_name, category, quantity, amount) VALUES (?, ?, ?, ?)', ("Ac","electronics",3,55330))
cursor.execute('INSERT INTO sales (product_name, category, quantity, amount) VALUES (?, ?, ?, ?)', ("Tv","electronics",3,55330))
cursor.execute('INSERT INTO sales (product_name, category, quantity, amount ) VALUES (?, ?, ?, ?)', ("pant","clothes",4,530))
cursor.execute('INSERT INTO sales (product_name, category, quantity, amount) VALUES (?, ?, ?, ?)', ("shirt","clothes",3,550))
cursor.execute('INSERT INTO sales (product_name, category, quantity, amount ) VALUES (?, ?, ?, ?)', ("sofa","furniture",4,530))
cursor.execute('INSERT INTO sales (product_name, category, quantity, amount) VALUES (?, ?, ?, ?)', ("Bed","furniture",3,5330))
cursor.execute('INSERT INTO sales (product_name, category, quantity, amount ) VALUES (?, ?, ?, ?)', ("Rice","grocery",4,530))
cursor.execute('INSERT INTO sales (product_name, category, quantity, amount) VALUES (?, ?, ?, ?)', ("wheat","grocery",3,5530))


# Commit the changes


cursor.execute('SELECT * FROM sales')

# Fetch results
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)



#conn.row_factory = sqlite3.Row
cursor.execute('SELECT SUM(amount) FROM sales')

# Fetch the result
total_amount = cursor.fetchone()[0]

print(f"Total Amount: {total_amount}")

# Close the connection



cursor.execute('SELECT SUM(amount * quantity) FROM sales')

# Fetch the result
total_revenue = cursor.fetchone()[0]

print(f"Total Revenue: {total_revenue}")

cursor.execute('''
    SELECT product_name, SUM(amount * quantity) AS total_sales
    FROM sales
    GROUP BY product_name
''')

# Fetch data
results = cursor.fetchall()

# Separate data for plotting
products = [row[0] for row in results]
sales = [row[1] for row in results]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(products, sales, color='skyblue')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.title('Total Sales by Product')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Close the connection
connection.close()