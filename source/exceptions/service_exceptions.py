class TransformCsvException(Exception):
    """Raised when loading the csv file into a dataframe"""

    def __init__(self, message="Error while creating all the tables of the DB"):
        self.message = message
        super().__init__(self.message)


class AddSaleServiceError(Exception):
    """Raised when adding a sale to db is not done correctly"""

    def __init__(self, message="Error while adding a sale occured"):
        self.message = message
        super().__init__(self.message)


class SaleValidationError(Exception):
    """Raised when converting the csv ro to a sale"""

    def __init__(self, message="Error while converting to a Sale object"):
        self.message = message
        super().__init__(self.message)
