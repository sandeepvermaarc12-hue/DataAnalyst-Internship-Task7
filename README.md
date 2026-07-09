# Task 7 - Basic Sales Summary from SQLite Database using Python

## Objective
Use SQL inside Python to pull simple sales info (total quantity sold, total revenue) 
from a tiny SQLite database, and display it using print statements and a bar chart.

## Tools Used
- Python 3
- sqlite3 (built-in)
- pandas
- matplotlib

## Dataset
A SQLite database file `sales_data.db` was created with a single `sales` table 
containing sample sales records across 5 products (Laptop, Mouse, Keyboard, Monitor, 
Headphones) with columns: id, product, quantity, price, sale_date.

## What I Did
1. Created a SQLite database (`sales_data.db`) using `create_db.py`, with a `sales` 
   table and sample sales data inserted.
2. Wrote `sales_summary.py` to connect to the database using Python's sqlite3 module.
3. Ran a SQL query using GROUP BY to calculate total quantity and revenue per product.
4. Ran a second query to get overall totals (units sold, total revenue).
5. Loaded results into a pandas DataFrame using pd.read_sql_query() and printed them.
6. Created a bar chart of Revenue by Product using matplotlib, saved as sales_chart.png.

## Files in this Repository
- `create_db.py` - creates the SQLite database and inserts sample data
- `sales_summary.py` - runs SQL queries, prints results, and generates the chart
- `sales_data.db` - the SQLite database file
- `sales_chart.png` - bar chart output (Revenue by Product)
- `README.md` - this file

## Sample Output
Overall Totals: 74 units sold, Rs. 424600 total revenue

## Key Learnings
- Connecting Python to SQLite using sqlite3.connect()
- Writing basic SQL queries with GROUP BY and SUM()
- Loading SQL query results directly into a pandas DataFrame
- Visualizing data with a matplotlib bar chart
- SQLite databases can also be opened and queried using DB Browser for SQLite 
  without writing any Python code

## Interview Questions & Answers

**1. How did you connect Python to a database?**
Using the built-in sqlite3 module: conn = sqlite3.connect("sales_data.db")

**2. What SQL query did you run?**
A SELECT query with SUM() and GROUP BY to get total quantity and revenue per 
product, and a second query for overall totals.

**3. What does GROUP BY do?**
It groups rows with the same value in a column (here, product) so aggregate 
functions like SUM() can be applied to each group separately.

**4. How did you calculate revenue?**
Revenue = quantity x price, calculated inside SQL as SUM(quantity * price).

**5. How did you visualize the result?**
Using df.plot(kind='bar', x='product', y='revenue') from pandas, then saved 
with plt.savefig().

**6. What does pandas do in your code?**
Pandas converts the SQL query result into a DataFrame, making it easy to view 
and plot the data.

**7. What's the benefit of using SQL inside Python?**
It combines SQL's querying power with Python's ability to further process, 
analyze, and visualize data - all in one automated script.

**8. Could you run the same SQL query directly in DB Browser for SQLite?**
Yes. DB Browser for SQLite lets you open the .db file, go to "Execute SQL", 
and run the same query directly to get identical results without Python.