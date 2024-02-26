from sqlalchemy import Column, String, DateTime, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SalesTable(Base):
    __tablename__ = "sales"
    sales_order_number = Column(String, primary_key=True, unique=True)
    sales_order_line_number = Column(Integer)
    order_date = Column(DateTime)
    customer_name = Column(String)
    email_address = Column(String)
    item = Column(String)
    quantity = Column(Integer)
    unit_price = Column(Float)
    tax_amount = Column(Float)

    def to_dict(self)->dict:
        """
        this is used to convert the returned object from the db to a dict
        :return: dict
        """
        obj_dict = self.__dict__
        filtered_dict = {key: value for key, value in obj_dict.items() if not key.startswith('_')}
        return filtered_dict