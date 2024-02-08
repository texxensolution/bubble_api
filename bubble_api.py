import requests
import json

class BubbleAPI:
    def __init__(self, base_url,token):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}  

    def send_request(self, method, endpoint="", data=None, json=None, files=None, headers=None):
        url = self.base_url + endpoint

        
        if headers:
            self.headers.update(headers)  
        response = requests.request(method, url, headers=self.headers, data=data, json=json, files=files)
        
        # successful or not
        if response.status_code in [200, 201]:
            try:
                response_json = response.json()
               
                return {"success": True, "data": response_json}
              
            except ValueError: 
                return {"success": response.ok, "data": response.text}
        else:
            return {"success": False, "error": response.text}

    def post(self, endpoint="", data=None, json=None, files=None):
        if json:
            self.headers['Content-Type'] = 'application/json'
        else:
            self.headers['Content-Type'] =  "text/plain"
        return self.send_request("POST", endpoint, data=data, json=json, files=files)

    def get(self, endpoint="", params=None):
        
        return self.send_request("GET", endpoint, data=params)

    def put(self, endpoint="", data=None, files=None):
        return self.send_request("PUT", endpoint, data=data, files=files)

    def delete(self, endpoint=""):
        return self.send_request("DELETE", endpoint)

# POST single sample
base_url = "https://app-2039494.bubbleapps.io/version-test/api/1.1/obj/" #apiendpoint change this
token="fe7dbda1" # api key change this
api = BubbleAPI(base_url,token)

# crc_info = {
#     "name": "name",
#     "points": 3,
    
# }
# response = api.post("", json=crc_info)
# print(response)

# # Success checking
# if response["success"]:
#     print("Request was successful:", response["data"])
# else:
#     print("Request failed:", response["error"])


# POST BATCH sample
    
# bulk_data = [
#     {"name": "jjj", "points": 15},
#     {"name": "irtorto", "points": 60,}
# ]


# bulk_payload = "\n".join(json.dumps(item) for item in bulk_data)

# bulk_response = api.post("/bulk", data=bulk_payload)
# print(bulk_response)


# if bulk_response["success"]:
#     print("Bulk request was successful:", bulk_response["data"])
# else:
#     print("Bulk request failed:", bulk_response["error"])


# #GET sample
print(api.get("?cursor=1&limit=100"))
    