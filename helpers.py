import random

# An object reference storing the Product ID for the order book.
productId = 'BTC-USD'

def getInitialState(n_bids: int = 5, n_asks: int = 5, product_id: str = productId) -> dict:
	"""Generates an initial state for the order book from exchange.

	Parameters
	----------
	n_bids : int, optional
		Number of bids to generate in the initial state (default is 5).
	n_asks : int, optional
		Number of asks to generate in the initial state (default is 5).
	product_id : str, optional
		ID of the product for which order book is being created.

	Returns
	----------
	initialState : dict
		A dictionary consisting initial state for the order book.
	"""

	initialState = {
		'product_id': product_id,
		'bids': [],
		'asks': []
	}
	for x in range(n_bids):
		price = random.uniform(10000.00, 20000.00)
		size = random.uniform(0.0, 1.0)
		initialState['bids'].append([price, size])
	
	for x in range(n_asks):
		price = random.uniform(10000.00, 20000.00)
		size = random.uniform(0.0, 1.0)
		initialState['asks'].append([price, size])

	return initialState


def getRandomChange(n_changes: int = 5, product_id: str = productId) -> dict:
	"""Generates a random set of changes to update the order book.

	Parameters
	----------
	n_changes : int, optional
		Number of changes to generate in this random change (default is 5).
	product_id : str, optional
		ID of the product for which order book is being updated.

	Returns
	----------
	randomChange : dict
		A dictionary consisting a random change for the order book.
	"""

	randomChange = {
		'product_id': product_id,
		'changes': []
	}
	for x in range(n_changes):
		type = random.choice(['buy', 'sell'])
		price = random.uniform(10000.00, 20000.00)
		size = random.uniform(0.0, 1.0)
		randomChange['changes'].append([type, price, size])
	
	return randomChange