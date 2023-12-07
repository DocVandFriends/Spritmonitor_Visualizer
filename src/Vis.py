import json
import pandas as pd
import login

API_URL = "https://api.spritmonitor.de/v1"
BEARER_TOKEN = login.bearer_token
APP_TOKEN = login.app_token

class client_car:
    def __init__(self, car_id, make, model, consumption, tripsum, quantitysum) -> None:
        self.car_id = car_id
        self.make = make
        self.model = model
        self.consumption = consumption
        self.tripsum = tripsum
        self.quantitysum = quantitysum
        self.get_data()
        
    
    def get_car_data(self, jsonfile):
        url = f"{API_URL}/vehicles.json"
        with open(jsonfile) as jsonfile:
            car_data = json.load(jsonfile)
            self.car_id = car_data['car_id']
            self.make = car_data['make']
            self.model = car_data['model']
            self.consumption = car_data['consumption']
            self.tripsum = car_data['tripsum']
            self.quantitysum = car_data['quantitysum']
            
    
            
        
class visualizer:
    def __init__(self) -> None:
        print("do_nothing")
        
   
