from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import urllib.request
from  helper import * 
import logging
import os
import time

class Init:

	def __init__(self):

		self.exchanges = get_exchanges()

		self.symbols_path = get_symbols_path()

		self.quote_path = get_quote_path()
		
		self.trading_list_flag = False

		self.trading_df = None

		self.current_symbols_path = get_current_symbols_path()


	def get_tradable_lists(self):

		try:
			for exchange in self.exchanges:
				url = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange="+exchange+"&render=download"

				urllib.request.urlretrieve(url,self.symbols_path+exchange+"_symbols.csv")

				print(exchange+" symbols download done!")

			self.trading_list_flag=True
				
		except:
			logging.critical("could not parse the tradable list from nasdaq websites!")

	def get_symbols(self):

		dfs = pd.DataFrame()

		if self.trading_list_flag==True:
			for csv_file in os.listdir(self.symbols_path):
				exchange = csv_file.split('_')[0]
				print(exchange)
				exchange_file = self.symbols_path + csv_file
				print(exchange_file)
				if os.path.isfile(exchange_file):
					df = pd.read_csv(exchange_file)
					df["Symbol"] = df["Symbol"].map(convert_symbol)
					df["Exchange"] = exchange
					#df = df[:2]
					dfs = pd.concat([dfs,df],axis=0,)
			dfs = dfs.reset_index()
			dfs = dfs.drop('index',1)
			dfs = dfs.drop('Unnamed: 8',1)
			dfs = dfs.replace('n/a',np.nan)
			#print(dfs)
			self.trading_df = dfs
			
		else:
			logging.critical("parse tradable list error!")

	def save_symbols(self):
		try:
			self.trading_df.to_csv(self.current_symbols_path+'current_symbols.csv')
		except:
			logging.critical("save trading symbols error!")
					
		


if __name__=="__main__":
	init = Init()
	init.get_tradable_lists()
	init.get_symbols()
	init.save_symbols()
