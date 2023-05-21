import time
import requests
import math
import random
 
TOKEN = "BBFF-2EC0JyessEv85ClLJH9p4LaopvMvza"  # Copier la valeur de ton TOKEN ici
DEVICE_LABEL = "Raspberry" # Label de la machine ou l’objet IOT qu’on va créer sur Ubidots
VARIABLE_LABEL_1 = "temperature"  # Label de la 1ière variable capturée
VARIABLE_LABEL_2 = "humidite"  # Label de la 2ième  variable capturée
VARIABLE_LABEL_3 = "position"  # Label de la 3ième variable capturée
 



 
def build_payload(variable_1, variable_2, variable_3):
    # Creates two random values for sending data
    value_1 = random.randint(-10, 50)   # calcul aléatoire de la température 
    value_2 = random.randint(0, 85)     # calcul aléatoire de l’humidité
 
    # Creates the gps coordinates
    lat = 34.757358   # valeur du latitude
              
    lng = 10.772115  # valeur du longitude
             
    payload = {variable_1: value_1,
               variable_2: value_2,
               variable_3: {"value": 34.10, "context": {"lat": lat, "lng": lng}}}
              # création du paylod, c’est le champ Data du message à envoyer
    return payload
 

def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
 
    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)
 
    # Processes results
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False
 
    print("[INFO] request made properly, your device is updated")
    return True
 
def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3)
 
    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")
 
if __name__ == '__main__':
    while (True):
        main()
        time.sleep(3)
     
     
     //BBFF-8v35CtRHnwu9QqvZocCTjCjn5yQjhu
