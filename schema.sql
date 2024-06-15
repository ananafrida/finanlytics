CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    date TEXT,
    amount REAL,
    category TEXT,
    description TEXT
);

INSERT INTO transactions (date, amount, category, description) VALUES
('2024-01-01', 100.0, 'Groceries', 'Walmart'),
('2024-01-02', 50.0, 'Transport', 'Bus ticket'),
('2024-01-03', 200.0, 'Rent', 'Monthly rent'),
('2024-02-01', 150.0, 'Groceries', 'Walmart'),
('2024-02-02', 60.0, 'Transport', 'Bus ticket'),
('2024-02-03', 210.0, 'Rent', 'Monthly rent'),
('2024-03-01', 120.0, 'Groceries', 'Walmart'),
('2024-03-02', 70.0, 'Transport', 'Bus ticket'),
('2024-03-03', 220.0, 'Rent', 'Monthly rent')
;


DELETE FROM transactions
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM transactions
    GROUP BY date, amount, category, description
);