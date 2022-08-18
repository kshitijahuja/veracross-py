# Veracross Data API v3

import requests
import time
class Client:    
    # Constructor
    def __init__(self, client_id, client_secret, school_route):
        self.client_id = client_id
        self.client_secret = client_secret
        self.school_route = school_route

    # Retrieve Access Token
    def get_access_token(self, scope):
        client_id = self.client_id
        client_secret = self.client_secret
        school_route = self.school_route
        school_base_url = 'https://accounts.veracross.com/'+school_route

        url_address = school_base_url+'/oauth/token' # Set destination URL here
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
            "scope": scope
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        resp = requests.post(url=url_address, headers=headers, data=data)

        # print(resp.__dict__)
        if( resp.status_code == 200):
            return resp.json()['access_token']
        else:
            return False
            
    # Rate Limiting
    def rate_limit(self, limit_balance):
        sleep_for = ((limit_balance) - time.time()) / 1000
        print(f"Sleeping for {sleep_for}")
        time.sleep(sleep_for)

    # List
    def list(self, scopes, path, params={}):
        client_id = self.client_id
        client_secret = self.client_secret
        school_route = self.school_route
        api_base_url = 'https://api.veracross.com/'+school_route+'/v3'

        if(scopes):

            access_token = self.get_access_token(scopes)
            if(access_token):
                url_address = api_base_url+'/'+path # Set destination URL here
                page_number = 1
                page_size = 1000
                all_records = []

                while(1):
                    headers = {
                        "Content-Type": "application/json",
                        "authorization": "Bearer "+ access_token,
                        "X-Page-Number": str(page_number),
                        "X-Page-Size": str(page_size)
                    }

                    resp = requests.get(url=url_address, headers=headers, params=params)
                    if(resp.status_code == 200):
                        # enforcing rate-limits                
                        if(int(resp.headers['X-Rate-Limit-Remaining']) == 1):
                            self.rate_limit(int(resp.headers['X-Rate-Limit-Reset']))

                        # increment page number
                        this_response = resp.json()['data']
                        all_records.append(this_response)
                        if(len(this_response) > page_size):
                            page_number += 1
                        else:
                            return all_records
                    else:                        
                        raise ValueError(f"API call failed with error code {resp.status_code}. Please refer API documentation.")
                        # return 'false' # error - http
            else:
                raise ValueError(f"Error retrieving access token.")
                # return 'false' # error - access token
        else:
            raise ValueError(f"Error setting the scopes.")
            # return 'false' # error - setting scopes


    # Read
    def read(self, scopes, path):
        client_id = self.client_id
        client_secret = self.client_secret
        school_route = self.school_route
        api_base_url = 'https://api.veracross.com/'+school_route+'/v3'

        if(scopes):
            access_token = self.get_access_token(scopes)
            if(access_token):
                url_address = api_base_url+'/'+path # Set destination URL here
                headers = {
                    "Content-Type": "application/json",
                    "authorization": "Bearer "+ access_token
                }

                resp = requests.get(url=url_address, headers=headers)
                if(resp.status_code == 200):
                    this_response = resp.json()['data']
                    return this_response
                else:                        
                    raise ValueError(f"API call failed with error code {resp.status_code}. Please refer API documentation.")
                    # return 'false' # error - http
            else:
                raise ValueError(f"Error retrieving access token.")
                # return 'false' # error - access token
        else:
            raise ValueError(f"Error setting the scopes.")
            # return 'false' # error - setting scopes
