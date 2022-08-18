# How to make READ calls
############################
# 1: Ensure config.py has the all the configurations from Veracross
import config
import veracross as v

# 2: Create a client
vc = v.Client(config.client_id, config.client_secret, config.school_route)

# 3: Specify scopes specific to the call you wish to make
# Note: ensure these client_id has been assigned these scopes in Veracross
scopes = "students:read"

# 4: finally, call the endpoint!
data = vc.read(scopes, "students/83000") # call the endpoint (from Veracross API docs that you wish to call eg. students/{id}, staff_faculty/{id} etc.)
# data = vc.read(scopes, "staff_faculty/10000") 
# data = vc.read(scopes, "parents/10000") 

if(data):
    print(data)
    # for record in data:
    #     print(f"{record['id']} | {record['first_name']} | {record['last_name']}")
else:
    print("No records found.")




