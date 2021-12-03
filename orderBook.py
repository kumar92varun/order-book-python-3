class OrderBook:
	"""A class to represent an order book.

	An order book is a list of trades, either electronic or manual, that an exchange uses to record market interest in a specific security or financial instrument.
	Shares are normally listed in an order book by volume and by price level.

	...
	Attributes
	----------
	bids : list
		List of bids sorted in descending order of the price for the order book.
	asks : list
		List of asks sorted in ascending order of the price for the order book.
	pricePrecision : int
		An integer value specifying decimal number precision while adding prices for a bid or an ask.
	sizePrecision : int
		An integer value specifying decimal number precision while adding size / quantity at a given price for a bid or an ask.
	
	Methods
	----------
	saveBids(bids)
		Saves a list of bids in self.bids attribute, then sorts the bids in descending order of the price value for a bid.
	saveAsks(asks)
		Saves a list of asks in self.asks attribute, then sorts the asks in ascending order of the price value for an ask.
	sortBids()
		Sorts the bids in self.bids attribute in descending order of the price value for a bid.
	sortAsks()
		Sorts the asks in self.asks attribute ascending order of the price value for an ask.
	updateBook(updates)
		Iterates through all the changes in order book and save them in either bids or asks.
	print()
		Prints a tabular representation of Buy and Sell for the order book.
	"""

	bids = []
	asks = []
	pricePrecision = 2
	sizePrecision = 8


	def __init__(self, data: dict) -> None:
		""" Special method to initialize data attributes of this class.

		Parameters
		----------
		data : dict, required
			A dictionary containing Product ID and initial bids and asks to initialize the order book class object.
		"""

		self.product_id = data['product_id']
		self.saveBids(data['bids'])
		self.saveAsks(data['asks'])


	def saveBids(self, bids: list) -> None:
		"""Saves a list of bids in self.bids attribute, then sorts the bids in descending order of the price value for a bid.

		Parameters
		----------
		bids : list, required
			A list of bids that needs to be updated in self.bids attribute.
		"""

		for bid in bids:
			price = round(float(bid[0]), self.pricePrecision)
			size = round(float(bid[1]), self.sizePrecision)
			self.bids.append([price, size])
		self.sortBids()


	def saveAsks(self, asks: list) -> None:
		"""Saves a list of asks in self.asks attribute, then sorts the asks in ascending order of the price value for an ask.

		Parameters
		----------
		asks : list, required
			A list of asks that needs to be updated in self.asks attribute.
		"""

		for ask in asks:
			price = round(float(ask[0]), self.pricePrecision)
			size = round(float(ask[1]), self.sizePrecision)
			self.asks.append([price, size])
		self.sortAsks()


	def sortBids(self) -> None:
		""" Sorts the bids in self.bids attribute in descending order of the price value for a bid. """

		self.bids = sorted(self.bids, key=lambda bid: bid[0], reverse=True)


	def sortAsks(self) -> None:
		""" Sorts the asks in self.asks attribute ascending order of the price value for an ask. """

		self.asks = sorted(self.asks, key=lambda ask: ask[0])


	def updateBook(self, updates: dict) -> None:
		"""Iterates through all the changes in order book and save them in either bids or asks.

		Parameters
		----------
		updates : dict, required
			A dictionary of changes that needs to be updated in the order book.
		"""

		newBids = []
		newAsks = []
		for (type, price, size) in updates['changes']:
			if type == 'buy':
				newBids.append([price, size])
			else:
				newAsks.append([price, size])
		self.saveBids(newBids)
		self.saveAsks(newAsks)
		self.printBook()


	def printBook(self) -> None:
		""" Prints a tabular representation of Buy and Sell for the order book. """

		print('\n' * 2)
		print("{: ^41}".format("Order Book for '" + self.product_id + "'"), end='\n')

		print("{: ^41}".format('Buy'))
		print('-' * 41)
		print("{: ^20}|{: ^20}".format('Price', 'Quantity'))
		print('-' * 41)
		for row in self.bids:
			print("{: ^20}|{: ^20}".format(*row))

		print('\n' * 1)

		print("{: ^41}".format('Sell'))
		print('-' * 41)
		print("{: ^20}|{: ^20}".format('Price', 'Quantity'))
		print('-' * 41)
		for row in self.asks:
			print("{: ^20}|{: ^20}".format(*row))