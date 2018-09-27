import sqlite3
import ftplib

try:
    ftp = ftplib.FTP('ftp3.interactivebrokers.com', 'shortstock', )
    ftp.retrbinary("RETR " + "usa.txt", open("usa_stock.txt", 'wb').write)
    ftp.quit()
except ConnectionRefusedError as ex:
    print("Could not retrieve data, Error {}".format(str(ex)))
except ftplib.error_perm as ex:
    print("Could not retrieve data, Error {}".format(str(ex)))

try:
    with open('usa_stock.txt', 'r') as f: # open the csv data file
        all_lines = f.readlines()
        lines = [] if len(all_lines) <=3 else all_lines[2:-1]

        sql = sqlite3.connect('db.sqlite3')
        cur = sql.cursor()
        cur.executescript('drop table if exists stocks_ticker;')
        cur.execute('''CREATE TABLE IF NOT EXISTS stocks_ticker
                    (symbol text, curency text, name text, con real, isin text, rebate_rate real, fee_rate real, amount text, space text)''')  # create the table if it doesn't already exist

        for line in lines:
            cur.execute("INSERT INTO stocks_ticker VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", line.split('|'))

        sql.commit()
        sql.close()
except FileNotFoundError as ex:
    print("File open error, Error {}".format(str(ex)))
except Exception as ex:
    print("Some error occured, Error {}".format(str(ex)))
    if sql.open():
        sql.close()

if __name__ == '__main__':
    try:
        sql = sqlite3.connect('db.sqlite3') # checking loaded data
        cur = sql.cursor()
        cur.execute("select * from stocks_ticker")
        for row in cur.fetchall():
            print(row)
        print("\n\nData loaded successfully")
    except sqlite3.OperationalError as ex:
        print("\n\nData load to the database failed, Error {}".format(str(ex)))