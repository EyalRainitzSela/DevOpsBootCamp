import logging
# from azure.storage.blob import BlobServiceClient
import azure.functions as func
# import os
# import json
# import requests
# connect_str = os.getenv('AzureWebJobsStorage')
# blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=staticonweb;AccountKey=yBRMqlUN1PcgvDbjes+fhuJlDqSMK2eZEhlotst3Gcrg2f5k/WbyV3zUHdEiEq+br4pPcuOAlAf3iOhshbHxrQ==;EndpointSuffix=core.windows.net')
# # blob_service_client = BlobServiceClient.from_connection_string(connect_str)
# container_client = blob_service_client.get_container_client("bootcampusers")
# blob_client = container_client.get_blob_client("users.json")


# def search_json(email,json_loads):
#     for i in json_loads:
#         if i['email'] == email:
#             return i['role']


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    email = req.params.get('email')
    if not email:
        try:
            req_body = req.get_json()
            print(req_body)
        except ValueError:
            pass
        else:
            email = req_body.get('email')
    try:
        # streamer = blob_client.download_blob()
        # filereader = json.loads(streamer.readall())
        # role = search_json(email,filereader)
        # return func.HttpResponse(json.dumps(role))
        return func.HttpResponse(email)
    except ValueError:
        pass
    return func.HttpResponse("error")
    # return func.HttpResponse(dict(blob_client))