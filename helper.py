import configparser

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
