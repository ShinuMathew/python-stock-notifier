import enum

class Stock(enum.Enum):
    INSTOCK = 'Instock'
    OUTOFSTOCK = 'OutOfStock'

class Status(enum.Enum):
    FAILURE = 'Failure'
    SUCCESS = 'Success'