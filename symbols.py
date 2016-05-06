from bs4 import BeautifulSoup
import urllib.request
from  helper import * 



print("test.................")

exchanges = get_exchanges()

symbols_path = get_symbols_path()


for exchange in exchanges:
	url = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange="+exchange+"&render=download"

	urllib.request.urlretrieve(url,symbols_path+exchange+"_symbols.csv")

	print(exchange+" symbols download done!")
