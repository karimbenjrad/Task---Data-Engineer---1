import io
import io
import os
from datetime import datetime, timedelta

from azure.storage.blob import BlobServiceClient, ContentSettings, generate_account_sas, ResourceTypes, \
    AccountSasPermissions
from fastapi import UploadFile

from configuration.configuration import setting_blob_storage

# Set the root directory that contains data to upload.
# Sub-directories of root will be created as containers.
# All files inside the container-folders will be uploaded as blobs.
# Azure Storage Account Name
# account_name = 'devstoreaccount1'
# # Azure Storage Account URL
# account_url = f'http://azurite:10000/{account_name}'
# # Account Key
# account_key = "Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw=="





async def upload_blob_from_uploadfile(file: UploadFile, blob_service_client: BlobServiceClient, destination_path: str = ""):
    container_name = "files"

    # Read the content of the uploaded file
    file_content = await file.read()

    # Combine the destination path with the filename to form the full blob name
    blob_name = os.path.join(destination_path, file.filename)

    # Upload the file content to Azure Blob Storage
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)
    content_settings = ContentSettings(content_type=file.content_type)
    blob_client.upload_blob(data=io.BytesIO(file_content), content_settings=content_settings)

sas_token = generate_account_sas(
    account_name=setting_blob_storage.ACCOUNT_NAME,
    account_key=setting_blob_storage.ACCOUNT_KEY,
    resource_types=ResourceTypes(object=True, container=True),
    permission=AccountSasPermissions(read=True, write=True, create=True, delete=True, list=True),
    expiry=datetime.utcnow() + timedelta(days=30)
)
b_s_c = BlobServiceClient(account_url=setting_blob_storage.ACCOUNT_URL,
                          credential=sas_token)


# upload_blob_from_uploadfile(file, b_s_c,destination_path="files")