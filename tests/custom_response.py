from fastapi import status, Response


def custom_client_response(status_val,response_data,return_payload=False):
    response: Response = Response
    if status_val:
        response.status_code = status.HTTP_201_CREATED
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return response