# How to make UPDATE calls
############################
# 1: Ensure config.py has the all the configurations from Veracross
import config
import veracross as v

# 2: Create a client
vc = v.Client(config.client_id, config.client_secret, config.school_route)

# 3: Specify scopes specific to the call you wish to make
# Note: ensure that this client_id has been assigned these scopes in Veracross as well
scopes = "emergency_contacts:update"

# 4: Set fields you wish to update
payload = {
    "data": {
        "first_name": "Saido",
        "middle_name": "",
        "last_name": "Farah",
        "postal_code": "02128"
    }
}

# 5: finally, call the endpoint!
data = vc.update(scopes, "emergency_contacts/1727245", payload)  # call the endpoint (in Veracross API docs these are the path like students, staff_faculty etc.)

if(data):
    print(f"Response to call: {data}") # a response code 204 means success!
else:
    print("No records found.")




