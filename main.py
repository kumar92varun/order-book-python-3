from helpers import *
from orderBook import OrderBook

initialState = getInitialState(n_bids = 3, n_asks = 5)
orderBook = OrderBook(initialState)

randomChange = getRandomChange(8)
orderBook.updateBook(randomChange)

randomChange = getRandomChange(2)
orderBook.updateBook(randomChange)

randomChange = getRandomChange(6)
orderBook.updateBook(randomChange)