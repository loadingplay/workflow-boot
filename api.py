import logging
from fastapi import FastAPI
from fastapi import HTTPException
from app.get_list_not_found import GetDocumentsNotFound
from app.retry_document import PostDocumentsNotFound

logging.getLogger().setLevel(logging.INFO)
api = FastAPI()


@api.post("/v1/get_document_failed")
def get_list_document_not_found(data: dict):
    logging.info(f"Arrived data list document : {data}")
    json_data = GetDocumentsNotFound(data)
    data_json = json_data.get_documents()
    logging.info(f"Output data list document : {data_json}")
    return data_json

@api.post("/v1/retry_document_failed")
def post_retry_document(data: dict):
    logging.info(f"Arrived data retry document : {data}")
    try:
        json_data = PostDocumentsNotFound(data)
        data_json = json_data.get_documents()
        logging.info(f"Output data retry document : {data_json}")
        return data_json
    except Exception as ex:
        logging.info(f"Error on retry document: {ex}")