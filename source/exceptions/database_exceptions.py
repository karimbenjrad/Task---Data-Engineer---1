class CreateAllTablesError(Exception):
    """Raised when creating all the tables of the DB is not done correctly"""

    def __init__(self, message="Error while creating all the tables of the DB"):
        self.message = message
        super().__init__(self.message)


class YieldingSessionError(Exception):
    """Raised when yielding a session for the DB is not done correctly"""

    def __init__(self, message="Error while yielding a session for the DB"):
        self.message = message
        super().__init__(self.message)



class AddSaleError(Exception):
    """Raised when adding a sale to db is not done correctly"""

    def __init__(self, message="Error while yielding a session for the DB"):
        self.message = message
        super().__init__(self.message)


class GetSaleError(Exception):
    """Raised when adding a sale to db is not done correctly"""

    def __init__(self, message="Error while yielding a session for the DB"):
        self.message = message
        super().__init__(self.message)


class GetSaleErrorService(Exception):
    """Raised when adding a sale to db is not done correctly"""

    def __init__(self, message="Error while yielding a session for the DB"):
        self.message = message
        super().__init__(self.message)
