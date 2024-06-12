import pytest
from . import request_response
from typing import Callable, Dict
from tests.fake_data import fake_data_obj
from pathlib import Path
import json
BASE_DIR: str = Path(__file__).resolve().parent



class TestEvents():
    
    @pytest.mark.parametrize(
		'params',
		[
			{
				'url': '/events/',
				'method': 'GET'
			}
		]
	)
    def test_get_all_event(
		self: object,
		request_response: Callable
	):
        '''
        	This function is used for getting list of event to test.
        '''
        assert request_response.status_code == 200, "status code should be 200"
    
    @pytest.mark.parametrize(
		'params',
		[
			{
				'url': '/events/',
				'method': 'POST',
				'payload': fake_data_obj.get_event_payload()
			}
		]
	)
    def test_create_event(
		self: object,
		request_response: Callable
	):
        '''
			This function is used for creating event.
        '''
        assert request_response.status_code == 201, "status code should be 201"
        data: Dict = request_response.json()
        with open(f"{BASE_DIR}/fake_data.json", "r") as json_data:
            data_obj: Dict = json.load(json_data)
        
        data_obj.update(
            {
                "id": data.get("id")
            }
		)
        with open(f"{BASE_DIR}/fake_data.json", "w") as json_file:
            json.dump(data_obj, json_file, indent=4)
    
    @pytest.mark.parametrize(
		'params',
		[
			{
				'url': f'/events/',
				'method': 'GET',
				'need_event_id': True
			}
		]
	)
    def test_get_event_detail(self: object, request_response: Callable) -> None:
        '''
        	This function is used for event by id.
        '''
        assert request_response.status_code == 200
    
    @pytest.mark.parametrize(
		'params',
		[
			{
				'url': f'/events/',
				'method': 'DELETE',
				'need_event_id': True
			}
		]
	)
    def test_delete_event(self: object, request_response: Callable) -> None:
        '''
        	This function is used for removing event.
        '''
        assert request_response.status_code == 200