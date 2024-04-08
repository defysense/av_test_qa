import requests
import sys
sys.path.append('../..')
from configuration import SERVICE_URL

def test_getting_card():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    response = requests.get(url=SERVICE_URL, headers=headers)
    assert response.status_code == 200, "Recieved status code is not equal to expected"
    
    # print(response.json())
    # print(response.status_code)
    # print(response.headers)
    # json_data = json.loads(response.text)
    # print(json_data)
    # print(f'Total users: {response.json().get("total")}')
    # print(requests.get(url='https://www.avito.ru/avito-care/eco-impact HTTP1.1/Content-Type:application/jsonAccept:application/json').content)
