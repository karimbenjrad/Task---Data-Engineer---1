from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi import UploadFile, File
from loguru import logger

from blob_storage.blob_storage import upload_blob_from_uploadfile,b_s_c
from configuration.injection import Container
from source.exceptions.database_exceptions import GetSaleErrorService
from source.exceptions.service_exceptions import AddSaleServiceError
from source.services.sales_service import SaleService

app_router = APIRouter()

@app_router.post("/ingest/")
@inject
async def ingest(files: List[UploadFile] = File(...), sales_service: SaleService = Depends(
    Provide[Container.sales_service])):
    """
    ingest multiple csv files
    """
    for file in files:
        try:

            result = sales_service.etl_pipeline(file.file)
            logger.info("file saved in the database")
            await upload_blob_from_uploadfile(file, b_s_c, destination_path="files")
            logger.info("file saved in the blob")
        except AddSaleServiceError as error:
            raise HTTPException(status_code=500, detail=f"file already exists: {str(error)}")
    return result


@app_router.get("/read/first-chunck")
@inject
async def get_last_rows(sales_service: SaleService = Depends(
    Provide[Container.sales_service])):
    """
    get first 10 rows from database
    """
    try:
        return sales_service.get_multiple_lines()
    except GetSaleErrorService as error:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(error)}")
