import configparser
import pandas as pd
import logging


def get_exchanges():
	Config = configparser.ConfigParser()

	Config.read("goldenwise.ini")


	exchanges = []


	for (each_key, each_val) in Config.items("Exchanges"):
        	if each_val not in exchanges:
                	exchanges.append(each_val)
	return exchanges

def get_symbols_path():
	symbols_path = ""

	Config = configparser.ConfigParser()

	Config.read("goldenwise.ini")

	for (each_key, each_val) in Config.items("Path"):
        	if each_key=="symbols":
                	symbols_path=each_val

	return symbols_path

def get_quote_path():
        quote_path = ""

        Config = configparser.ConfigParser()

        Config.read("goldenwise.ini")

        for (each_key, each_val) in Config.items("Path"):
                if each_key=="quote":
                        quote_path=each_val

        return quote_path

def get_current_symbols_path():
        current_symbols_path = ""

        Config = configparser.ConfigParser()

        Config.read("goldenwise.ini")

        for (each_key, each_val) in Config.items("Path"):
                if each_key=="current_symbols":
                        current_symbols_path=each_val

        return current_symbols_path

def get_current_symbols_file_name():

	filename = None

	path = get_current_symbols_path()

	Config = configparser.ConfigParser()

	Config.read("goldenwise.ini")

	for (each_key, each_val) in Config.items("File"):
		if each_key=="current_symbols":
			filename = path + each_val
	return filename

	


def convert_symbol(symbol):
	return symbol.strip().upper()

def load_current_symbols():

	try:
		df = pd.read_csv(get_current_symbols_file_name())
	except:
		logging.critical("load current symbols error!")






def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

if __name__=="__main__":
	print(convert_symbol("  heLLo "))
	print(get_current_symbols_path())
	print(get_current_symbols_file_name())
	load_current_symbols()
