#all http requests will be written here
import requests
import yaml
from requests.exceptions import HTTPError

with open('src/config/config.yml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    yml_content = yaml.load(file, Loader=yaml.FullLoader)

params = {
  "Authentication": "Bearer "+yml_content['jwt_token']
}
base_url = yml_content['api_base_url']
#base_url = "http://localhost:8000"
full_url = base_url + '/api/users/recommender'

def get_recommender_data():
  try:
    response = requests.get(full_url, params=params)
    # If the response was successful, no Exception will be raised
    response.raise_for_status()
  except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
    return 0
  except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
    return 0
  else:
    print('Success!')
    return response.json()