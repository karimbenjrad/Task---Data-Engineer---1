from pydantic import BaseModel, Field
from datetime import datetime


class Sale(BaseModel):
    sales_order_number: str = Field(description="Sales Order Line Number")
    sales_order_line_number: int = Field(description="Sales Order Line Number")
    order_date: datetime = Field(description="Order Date")
    customer_name: str = Field(description="Customer Name")
    email_address: str = Field(description="Email Address")
    item: str = Field(description="Item")
    quantity: int = Field(description="Quantity")
    unit_price: float = Field(description="Unit Price")
    tax_amount: float = Field(description="Tax Amount")
