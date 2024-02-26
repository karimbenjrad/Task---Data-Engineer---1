from typing import List

from pydantic import ValidationError

from configuration.configuration import csv_config
from schema.data_schemas import Sale
from source.exceptions.database_exceptions import AddSaleError, GetSaleError, GetSaleErrorService
from source.exceptions.service_exceptions import TransformCsvException, AddSaleServiceError, SaleValidationError
from source.queries.sales_queries import SalesCrud
from pandas import read_csv
from os import listdir
from loguru import logger
from source.utils import camelcase_to_snakecase


class SaleService:
    def __init__(self, sale_crude: SalesCrud):
        self.sale_crude = sale_crude

    def add_sale(self, sale: Sale) -> Sale:
        """
        add a sale to database
        :param sale: a sale model
        :return: a sale
        """
        try:
            return self.sale_crude.add_sale(sale)
        except AddSaleError as error:
            raise AddSaleServiceError("error n service while adding sale to db") from error

    def add_multiple_sales(self, sales: List[Sale]) -> List[Sale]:
        """
        add a sale to database
        :param sale: a sale model
        :return: a sale
        """
        try:
            return self.sale_crude.add_multiple_sales(sales)
        except AddSaleError as error:
            raise AddSaleServiceError("error n service while adding sale to db") from error

    def extract_from_one_or_more_csv(self) -> List[Sale]:
        """
        transform csv into a list of sale object
        :param file_path: csv file path
        :return: list of sale
        """
        result_list = []
        for file_name in listdir(csv_config.CSV_DATA_PATH):
            try:
                sales_dataframe = read_csv(csv_config.CSV_DATA_PATH + file_name)
            except FileNotFoundError as error:
                raise AddSaleError("reading csv file failed") from error
            sales_dataframe.columns = [camelcase_to_snakecase(col) for col in sales_dataframe.columns]
            extracted_csv = sales_dataframe.to_dict(orient='records')

            try:
                extracted_csv = [Sale(**sale) for sale in extracted_csv]
            except ValidationError as error:
                raise AddSaleError(f"the schema of the csv file is invalid{extracted_csv[0]}") from error
            result_list.extend(extracted_csv)
        return result_list

    def etl_pipeline(self) -> None:
        """
        extract, transform and load csv file to db
        :return: True if the etl pipeline is ran successfully
        """
        sales_list = self.extract_from_one_or_more_csv()
        for sale in sales_list:
            self.add_sale(sale)
        # self.add_multiple_sales(sales_list)

    def get_multiple_lines(self) -> List[Sale]:
        try:
            sales = self.sale_crude.get_multiple_sales(limit=10)
            logger.info(sales)
        except GetSaleError as error:
            raise GetSaleErrorService("error while getting the sales") from error

        return [Sale(**sale) for sale in sales]
