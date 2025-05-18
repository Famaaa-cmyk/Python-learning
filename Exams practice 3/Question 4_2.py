import sqlite3

conn = sqlite3.connect('Rental.db')
cor = conn.cursor()


Command = """
CREATE TABLE IF NOT EXISTS rent (
    reg_number VARCHAR(50) PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status VARCHAR(20),
    total_cost DECIMAL(10, 2)
)"""
cor.execute(Command)
conn.commit()

def data_entry(reg,name,start_date,end_date,status,total_cost):
    command = f"""
    INSERT INTO rent (
        reg_number,
        customer_name,
        start_date,
        end_date,
        status,
        total_cost
    ) VALUES (
        '{reg}',
        '{name}',
        '{start_date}',
        '{end_date}',
        '{status}',
        {total_cost}
        );
        """
    return command

def show_data():
    command = "SELECT * FROM rent"
    s = cor.execute(command)
    data = s.fetchall()
    for i in data:
        print(i)
    



# command = data_entry('car001','ali','2025-05-10', '2025-05-12', 'Active', '123')
# cor.execute(command)
# conn.commit()

show_data()

# wehn we have below kindof data if i want to see car002 hwo to show it 