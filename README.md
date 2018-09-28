# Cost2Short
A Django application to work with stock loan data.

To run the django project please clone the repo and run pip install -r requirements.txt

The script `load_ticker_data.py` retrieves stock loan data from the ftp site ftp://ftp3.interactivebrokers.com and loads into a SQLite3 database. To run the script cd in to the folder where the script is located and run the following command

python load_ticker_data.py (Note: python should be running on the machine)

The index view of the django application reads and displays a list of all the stocks retrieved from the database. The url for this page is: http://localhost:8000/stocksStock.  The stock names in the list are linked to the stock details page so clicking on a name navigates to the stock detail page of that stock. Alternatively, any specifc ticker symbol can be displayed by passing the ticker symbol as a parameter to the following url.

http://localhost:8000/stocks/detail/<symbol>
