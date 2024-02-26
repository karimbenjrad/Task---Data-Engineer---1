from typing import Callable, ContextManager, List
from loguru import logger

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from schema.data_schemas import Sale
from source.database.database_models import SalesTable
from source.exceptions.database_exceptions import AddSaleError, GetSaleError


class SalesCrud:
    def __init__(self, session_factory: Callable[..., ContextManager[Session]]):
        self.session_factory = session_factory

    def add_multiple_sales(self, sales: List[Sale]) -> List[Sale]:
        """
                add sale to database
                :return: success/error message
        """
        new_file = [SalesTable(**sale.dict()) for sale in sales]
        try:
            with self.session_factory() as session:
                session.add_all(sales)
                session.commit()
                session.refresh(new_file)
                return new_file
        except SQLAlchemyError as integrity_error:
            raise AddSaleError from integrity_error

    def add_sale(self, sale: Sale) -> Sale:
        """
                add sale to database
                :return: success/error message
        """
        try:
            with self.session_factory() as session:
                new_file = SalesTable(**sale.dict())
                session.add(new_file)
                session.commit()
                session.refresh(new_file)
                return new_file
        except SQLAlchemyError as integrity_error:
            raise AddSaleError from integrity_error

    def get_multiple_sales(self, limit: int = 10) -> List[dict]:
        """
        Get the first 'limit' number of sales from the database.
        :param limit: Number of sales to retrieve (default is 10).
        :return: List of Sale objects.
        """
        try:
            with self.session_factory() as session:
                sales = session.query(SalesTable).limit(limit).all()
                logger.info(sales)
                return [sale.to_dict() for sale in sales]
        except SQLAlchemyError as integrity_error:
            raise GetSaleError from integrity_error
