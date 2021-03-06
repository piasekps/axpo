from typing import Dict

import requests

from cars.exceptions import NotFoundError


class NHTSAClient:
    def __init__(self) -> None:
        self.url = 'https://vpic.nhtsa.dot.gov/api/'
        self.name = 'NHTSA'

    def _get_request(self, path, response_format='json') -> Dict:
        # TODO: Additional connection errors should be catch and properly handle
        response = requests.get(f"{self.url}{path}?format={response_format}")

        assert response.status_code == 200
        result = response.json()

        if result['Count'] == 0:
            raise NotFoundError

        return result

    def get_models_by_name(self, model_name: str) -> Dict:
        """Get model list for given vehicle

        API Response for /vehicles/GetModelsForMake/Honda:
        {
            'Count': 438,
            'Message': 'Response returned successfully',
            'SearchCriteria': 'Make:Honda',
            'Results': [{
                'Make_ID': 474,
                'Make_Name': 'HONDA',
                'Model_ID': 1861,
                'Model_Name': 'Accord'
            }]
        }

        Results:
            {
                'Honda': {
                    [{
                        'Make_ID': 474,
                        'Make_Name': 'HONDA',
                        'Model_ID': 1861,
                        'Model_Name': 'Accord'
                    }]
                }
            }
        """
        response = self._get_request(f'/vehicles/GetModelsForMake/{model_name}')
        return {item['Model_Name'].upper(): item for item in response['Results']}
