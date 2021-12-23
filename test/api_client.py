# API Client for the open-elecbay app

# This client will simulate what a connected meter should be doing
# the meter will read the net flow of energy in and out of the home
# the net flow of energy is negative when the meter is running backwards
# that measn the meter is connected to a prosumer with the ability to
# generate energy from the connected system.
# the meter should just send the data to the system


# enrollment process for the mmeter to be onboarded to the system?
# management component?
# lets jsut try to get the user on the system

import requests
import json
import random
import time


def main():
    sim_cycles = 2
    sim_delay_sec = 10
    for lp in range(sim_cycles):
        for customer in range(5):
            r = create_market_msg(generate_data("000"+str(customer)))
        time.sleep(sim_delay_sec)
    print("done")


def generate_data(id):
    # generate the data
    # use the data from this exact time last year to generate the data
    baseload = 10
    net_energy = baseload + random.randint(0, 5)
    data = json.dumps({'customerID': id, 'kW': net_energy})
    return data


def create_market_msg(message):
    data = {'type': 'INFO', 'message': message}
    print(data)
    print("sending the data ")
    # create the request
    url = 'http://localhost:5001/request'
    resp = api_call(url, data=data)
    reqId = resp['id']
    print(reqId)
    # submit it to the market
    url = 'http://localhost:5001/submit/' + reqId
    resp = api_call(url, data='')
    print(resp)
    return resp


def api_call(url, data=None):
    try:
        if data is None:
            response = requests.get(
                url, timeout=5)
        else:
            response = requests.post(
                url=url, json=data, timeout=5)
        response.raise_for_status()
        # Code here will only run if the request is successful
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)


if __name__ == "__main__":
    main()
