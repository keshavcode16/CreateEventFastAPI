from typing import Dict, Union
import pytest
import json
from app.main import app
from fastapi.testclient import TestClient
from pathlib import Path
from typing import Optional, Any, Dict, List, Union


BASE_DIR: str = Path(__file__).resolve().parent
JSONObject: Dict = Dict[str, Any]

async def override_dependency(q: Optional[str] = None):
    pass


@pytest.fixture
def request_response(params: Dict) -> object:
    """
        This custom fixture will make request to the given endpoint and return status code.
    """
    with open(f"{BASE_DIR}/fake_data.json", "r") as json_data:
        data: Dict = json.load(json_data)
    
    url: Union[str, None] = params.get('url')
    headers: None = None
    method: Union[str, None] = params.get('method')
    payload: Union[Dict, None] = params.get('payload')
    need_event_id: Union[str, None] = params.get('need_event_id')
    
    if need_event_id:
        url += data.get("id")

    # api_client_handler = params.get('api_client_handler')
    # app.dependency_overrides[api_client_handler.auth_wrapper] = override_dependency
    client: TestClient = TestClient(app)

    if payload is None:
        payload: Dict = {}

    # headers: Dict = {'Authorization': f'Bearer mynewtoken'}

    
    if method == 'GET':
        response: object = client.get(
            url=url,
            # headers= headers
        )
    elif method == 'POST':
        response: object = client.post(
			url=url,
			data=json.dumps(payload),
			# headers=headers
        )
    elif method == 'DELETE':
        response: object = client.delete(
            url=url,
            headers=headers
        )
        
    #so on if any other request type contain....

    return response