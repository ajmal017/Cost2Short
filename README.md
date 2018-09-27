# Cost2Short
A Django application to work with stock loan data.
The script load_ticker_data.py retrieves stock loan data from the ftp site ftp://ftp3.interactivebrokers.com and loads into a SQLite3 database. To run the script cd in to the folder where script is located and run the following command

python load_ticker_data.py (Note: python shoul be running on the machine)

The index view  of the django application reads and displays first recod in the query set. Any specifc ticker symbol can be 
displayed by passing the ticker symbol as a parameter to the following url.
http://localhost:8000/stocks/detail/<symbol>
