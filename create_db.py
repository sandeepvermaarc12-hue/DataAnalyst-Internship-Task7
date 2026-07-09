import sqlite3

conn = sqlite3.connect("sales_data.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS sales")
cur.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    sale_date TEXT
)
""")

sample_data = [
    ('Laptop', 3, 55000, '2025-01-05'),
    ('Laptop', 2, 55000, '2025-01-12'),
    ('Mouse', 10, 500, '2025-01-06'),
    ('Mouse', 15, 500, '2025-01-15'),
    ('Keyboard', 8, 1200, '2025-01-07'),
    ('Keyboard', 5, 1200, '2025-01-18'),
    ('Monitor', 4, 9000, '2025-01-08'),
    ('Monitor', 6, 9000, '2025-01-20'),
    ('Headphones', 12, 1500, '2025-01-09'),
    ('Headphones', 9, 1500, '2025-01-22'),
]

cur.executemany("INSERT INTO sales (product, quantity, price, sale_date) VALUES (?, ?, ?, ?)", sample_data)
conn.commit()
conn.close()
print("sales_data.db created successfully!")