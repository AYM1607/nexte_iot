import requests

url = 'http://13.52.96.154/readings'


def sendMeterData(meterId, payload):
    payload['meter_id'] = meterId
    r = requests.post(url, json=payload)
    return r.status_code
