import requests
import json


if __name__ == '__main__':
    print('Attempting query #1 with sender_id=C1305486145:')
    r = requests.post('http://localhost:5050', data={'query_type': 'fraudulent', 'sid': 'C1305486145'})
    print(json.loads(r.text))

    print('Attempting query #2 with sender_id=C1305486145:')
    r = requests.post('http://localhost:5050', data={'query_type': 'highest', 'sid': 'C1305486145'})
    print(json.loads(r.text))

    print('Attempting query #3 with receiver_id=C553264065, start_date=2022-05-01, end_date=2022-07-01:')
    r = requests.post('http://localhost:5050', data={'query_type': 'date_sum', 'rid': 'C553264065',
                                                     'start_date': '2022-05-01', 'end_date': '2022-07-01'})
    print(json.loads(r.text)[0][0])
