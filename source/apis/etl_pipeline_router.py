from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi import UploadFile, File

from configuration.injection import Container
from source.exceptions.database_exceptions import GetSaleErrorService
from source.exceptions.service_exceptions import AddSaleServiceError
from source.services.sales_service import SaleService

app_router = APIRouter()

# @app_router.post("/ingest/")
# @inject
# async def ingest(sales_service: SaleService = Depends(
#                                              Provide[Container.sales_service])):
#     """
#     ingest multiple csv files
#     """
#     try:
#         sales_service.etl_pipeline()
#     except AddSaleServiceError as error:
#         raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(error)}")

@app_router.post("/ingest/")
@inject
async def ingest(files: List[UploadFile] = File(...), sales_service: SaleService = Depends(
                                             Provide[Container.sales_service])):
    """
    ingest multiple csv files
    """
    try:
        sales_service.etl_pipeline(files)
    except AddSaleServiceError as error:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(error)}")


@app_router.get("/read/first-chunck")
@inject
async def ingest(sales_service: SaleService = Depends(
                                             Provide[Container.sales_service])):
    """
    ingest multiple csv files
    """
    try:
        return sales_service.get_multiple_lines()
    except GetSaleErrorService as error:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(error)}")