import hashlib
import hmac
import requests
import time
import ssl
import json


access_key = '123456789'
secret_key = '123456789'



# 0. making ssl context - verify should be turned off
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# ------------------
# Get markets list
# ------------------



# 1. list markets
def get_markets():
	epoch_time = str(int(time.time()))+'000'
	request = 'access_key=' + access_key + '&tonce=' + epoch_time
	message = 'GET|/api/v2/markets|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
    		secret_key_bytes,
    		message_bytes,
    		hashlib.sha256
	).hexdigest()

# 1.2 list markets
	query = 'https://graviex.net/api/v2/markets?' + (request) + '&signature=' + (signature)

	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)
#https://tradesatoshi.com/api/public/getticker?market=LTC_BTC

def get_ticker():
	epoch_time = str(int(time.time()))+'000'
	request = 'access_key=' + access_key + '&tonce=' + epoch_time
	message = 'GET|/api/v2/tickers|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
    		secret_key_bytes,
    		message_bytes,
    		hashlib.sha256
	).hexdigest()

# 1.2 list markets
	query = 'https://graviex.net/api/v2/tickers?' + (request) + '&signature=' + (signature)

	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)





#https://graviex.net/documents/api_v2?lang=en
def get_orderbook(market):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key +'&market='+market+ '&tonce=' + epoch_time
	message = 'GET|/api/v2/order_book|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
        	message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/order_book?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)

def buy_limit(market, quantity, rate):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key + '&market='+market+'&price='+rate+'&side=buy' + '&tonce=' + epoch_time + '&volume='+quantity
	message = 'GET|/api/v2/orders|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
    	).hexdigest()

# 1.2 list markets
	query = 'https://graviex.net/api/v2/orders?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)



def sell_limit(market, quantity, rate):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key + '&market='+market+'&price='+rate+'&side=sell' + '&tonce=' + epoch_time + '&volume='+quantity
	message = 'GET|/api/v2/orders|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/orders?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)

def cancel(uuid):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key + '&id='+uuid+'&tonce=' + epoch_time
	message = 'GET|/api/v2/order/delete|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/delete?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)

def get_open_orders(market):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key + '&market='+market+'&tonce=' + epoch_time
	message = 'GET|/api/v2/orders|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/orders?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)

def get_balances():
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key + '&tonce=' + epoch_time
	message = 'GET|/api/v2/members/me|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/members/me?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)

def get_balance(ccy):
	dat=json.loads(get_balances())
	data=dat['accounts']
	i=0
	while(data[i]['currency']!=ccy):
		i+=1
	return float(data[i]['balance'])
    
    
def get_deposits():
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key + '&tonce=' + epoch_time
	message = 'GET|/api/v2/deposits|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/deposits?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)
 
def get_deposit(txid):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key +'&txid='+txid +'&tonce=' + epoch_time
	message = 'GET|/api/v2/deposit|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/deposit?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)

def get_deposit_address(ccy):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key +'&currency='+ccy+ '&tonce=' + epoch_time
	message = 'GET|/api/v2/deposit_address|' + request
#    secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/deposit_address?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)

def get_orders_multi(market,orders,orderSide,orderVolume,ordersPrice):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key +'&market='+market +'&orders[side]='+orderSide+'&orders[volume]='+ orderVolume+'orders[price]='+ordersPrice +'&tonce=' + epoch_time
	message = 'GET|/api/v2/orders/multi|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/orders/multi?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)



def get_orders_clear():
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key + '&tonce=' + epoch_time
	message = 'POST|/api/v2/orders/clear|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/orders/clear?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)


def get_depth(market):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key +'&market='+ market+'&tonce=' + epoch_time
	message = 'GET|/api/v2/depth|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/depth?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)


def get_trades(market):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key +'&market='+ market+'&tonce=' + epoch_time
	message = 'GET|/api/v2/trades|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()

# 1.2 list markets
	query = 'https://graviex.net/api/v2/trades?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)

def get_my_trades(market):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key +'&market='+ market+'&tonce=' + epoch_time
	message = 'GET|/api/v2/trades/my|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/trades/my?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)

def get_k(market):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key +'&market='+ market+'&tonce=' + epoch_time
	message = 'GET|/api/v2/k|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/k?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)


def get_k_with_pending_trades(market, trade_id):
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key +'&market='+market+'&trade_id='+trade_id+'&market='+ market+'&tonce=' + epoch_time
	message = 'GET|/api/v2/k_with_pending_trades|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
		hashlib.sha256
	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/k_with_pending_trades?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)

def get_timestamp():
	epoch_time = str(int(time.time())) + '000'
	request = 'access_key=' + access_key +'&tonce=' + epoch_time
	message = 'GET|/api/v2/timestamp|' + request
	secret_key_bytes= bytes(secret_key , 'latin-1')
	message_bytes = bytes(message, 'latin-1')
# 1.1 generate the hash.
	signature = hmac.new(
		secret_key_bytes,
		message_bytes,
			hashlib.sha256
	    	).hexdigest()
# 1.2 list markets
	query = 'https://graviex.net/api/v2/timestamp?' + (request) + '&signature=' + (signature)
	r = requests.get(query)
	data = json.loads(r.content.decode('utf-8'))
	return(data)


def get_HistoricalTrades(market):
	time.sleep(1)
	data=get_trades(market)
	time.sleep(1)
	try:
		dat=json.loads(data)
	except:
		return 0
	n=len(dat)
	history={}
	for i in range(0,n):
		info={}
		info['timestamp']=dat[i]['at']
		info['price']=float(dat[i]['price'])
		info['type']=None
		info['id']=dat[i]['id']
		info['quantity']=float(dat[i]['volume'])
		history[i]=info
	if(history=={}):
		return 0
	return(history)


def get_Volume_24h(market):
	time.sleep(1)
	data=get_HistoricalTrades(market)
	time.sleep(1)
	f=time.time()
	try:
		tim=data[0]['timestamp']
	except:
		return(0,0,0.5,0.5)
	i=1
	sumx=0
	sumc=0
	while(((f-tim)/(24*3600))<1):
		sumx+=data[i]['quantity']
		sumc+=data[i]['quantity']*data[i]['price']
		i+=1
		tim=data[i]['timestamp']
	return(sumx,sumc,0.5,0.5)


