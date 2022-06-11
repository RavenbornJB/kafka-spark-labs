import requests
import json


if __name__ == '__main__':
    print('Attempting query #1 with sender_id=C2050625634:')
    r = requests.post('http://localhost:5050', data={'query_type': 'fraudulent', 'sid': 'C2050625634'})
    print(json.loads(r.text))

    print('Attempting query #2 with sender_id=C2050625634:')
    r = requests.post('http://localhost:5050', data={'query_type': 'highest', 'sid': 'C2050625634'})
    print(json.loads(r.text))

    print('Attempting query #3 with receiver_id=C747551263, start_date=2022-05-20, end_date=2022-06-05:')
    r = requests.post('http://localhost:5050', data={'query_type': 'date_sum', 'rid': 'C747551263',
                                                     'start_date': '2022-05-20', 'end_date': '2022-06-05'})
    print(json.loads(r.text)[0][0])
