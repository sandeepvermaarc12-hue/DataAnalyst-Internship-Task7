import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to the database
conn = sqlite3.connect("sales_data.db")
print("Connected to sales_data.db successfully.\n")

# Step 2: SQL Query - total quantity & revenue per product
query1 = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
"""

df = pd.read_sql_query(query1, conn)
print("=== Sales Summary by Product ===")
print(df)
print()

# Step 3: SQL Query - overall totals
query2 = """
SELECT SUM(quantity) AS total_units_sold,
       SUM(quantity * price) AS total_revenue
FROM sales
"""

df_totals = pd.read_sql_query(query2, conn)
print("=== Overall Totals ===")
print(df_totals)
print()

# Step 4: Bar chart - revenue by product
df.plot(kind="bar", x="product", y="revenue", legend=False, color="skyblue")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("sales_chart.png")
print("Chart saved as sales_chart.png")

# Step 5: Close connection
conn.close()
print("\nDatabase connection closed.")