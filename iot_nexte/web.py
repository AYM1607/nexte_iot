import requests

url = 'http://api.next-e.mx/readings'


def sendMeterData(meterId, payload):
    payload['meter_id'] = meterId
    r = requests.post(url, json=payload)
    return r.status_code
