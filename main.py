import requests
import json
from beepy import beep
import time
from win10toast import ToastNotifier

wallet_address = '9fuoqNLuFea3ghYQsR9Hv1NU9AWsLjDrKU4fC1CKKQKLhJLmvyj'
worker_uri = f'https://api.nanopool.org/v1/ergo/workers/{wallet_address}'

while True:
    toast = ToastNotifier()
    worker_response = requests.get(worker_uri)
    parsed_workers = json.loads(worker_response.text)
    workers_data = parsed_workers['data']

    for worker_data in workers_data:
        if worker_data['hashrate'] == 0:
            for i in range(1000):
                toast.show_toast("Notification", "WANGGGGGGGGGGGGGGG RIG DOWNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
                                 duration=20)
                beep(sound="ping")
                time.sleep(1)
    time.sleep(30)
