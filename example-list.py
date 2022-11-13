# How to make LIST calls
############################
# 1: Ensure config.py has the all the configurations from Veracross
import config
import veracross as v

# 2: Create a client
vc = v.Client(config.client_id, config.client_secret, config.school_route)

# 3: Specify scopes specific to the call you wish to make
# Note: ensure that this client_id has been assigned these scopes in Veracross as well
scopes = "staff_faculty:list"

# 4: List call may include params (optional)
params = {
    "faculty_type": "2"
}

# 5: finally, call the endpoint!
data = vc.list(scopes, "staff_faculty") # call the endpoint (in Veracross API docs these are the path like students, staff_faculty etc.)
# more examples:
# data = vc.list(scopes, "students") 
# data = vc.list(scopes, "parents") 

if(data):
    print(data)
    # for record in data:
    #     print(f"{record['id']} | {record['first_name']} | {record['last_name']}")
else:
    print("No records found.")




