import ccxt

# 创建交易所实例
binance = ccxt.binance()

# 获取市场信息
markets = binance.load_markets()

# 获取特定交易对的行情
ticker = binance.fetch_ticker('BTC/USDT')import ccxt

# 创建交易所实例
binance = ccxt.binance()

# 获取市场信息
markets = binance.load_markets()

# 获取特定交易对的行情
ticker = binance.fetch_ticker('BTC/USDT')
