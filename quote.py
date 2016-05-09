from helper import *
import pandas_datareader.data as web
import datetime

import pandas as pd

import logging
import time
from joblib import Parallel,delayed


class quote_downloader():

	def __init__(self,start,end,mode="INC"):
		self.mode = mode
		self.start = start
		self.end = end
		break_symbol = read_break_downloading_symbol()
		self.symbols =  make_download_list(break_symbol)
		#self.symbols = self.symbols[:10]
		self.datasource = 'yahoo'
		#print(self.symbols)
		self.failed_symbols = []

		self.quote_path = get_quote_path()
		self.current_download_symbol = None

	def parallel_down(self):
		try:
			Parallel(n_jobs=2)(delayed(self.get_quote)(symbol) for symbol in self.symbols)
		except:
			write_break_downloading_symbol(self.current_download_symbol)
			logging.critical("parallel process error")
			sys.exit(1)
			
		
	

	def get_quote(self,symbol):

		try:
			time.sleep(0.01)	
			df = web.DataReader(symbol, self.datasource, self.start, self.end)
			df.to_csv(self.quote_path+symbol+".csv")
			print(symbol+" process done!")
			self.current_download_symbol = symbol
			
			
		except:
			logging.warning(symbol+" download historical data error!")
			self.failed_symbols.append(symbol)

	
		



if __name__=="__main__":

	start = datetime.datetime(2010, 1, 1)

	end = datetime.datetime(2016, 5, 7)

	dd = quote_downloader(start,end)

	dd.parallel_down()
