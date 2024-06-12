from typing import Dict
from pathlib import Path
import json

BASE_DIR: str = Path(__file__).resolve().parent

with open(f"{BASE_DIR}/fake_data.json", "r") as json_data:
        data: Dict = json.load(json_data)


class FakeData(object):
    
    def get_event_payload(self, is_updated=False) -> Dict:

        with open(f"{BASE_DIR}/fake_data.json", "r") as json_data:
            data: Dict = json.load(json_data)
        
        return data


fake_data_obj: FakeData = FakeData()
