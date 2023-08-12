
from robot.api.deco import keyword
import json
import requests
from requests import Response

class RemoveAgentTA:

    @keyword
    def remove_agent_api(self, uid: str):
        url = f"https://qa.letsdochinese.com/userconfigserver/admin/update/user/teams"
        headers = {
            'Authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhY2FsaW1hZyIsImlhdCI6MTY5MDUzOTAyOH0.STxpE7wfTbuvucPK5IV8Uzaxrx599Qlbidar1E2X9Dg",
            'Content-Type': "application/json"
        }

        payload = [
            {
                "uid": uid,
                "teamId": None
            }
        ]

        response = requests.put(url, headers=headers, json=payload)

        if response.text:  # Check if response content is not empty
            try:
                response_json = response.json()
                return response_json
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        else:
            print("Empty response content")
        
        # return None
        return response.status_code







# from contextlib import nullcontext
# from robot.api.deco import library, keyword
# import json
# import requests
# from RequestsLibrary.SessionKeywords import SessionKeywords
# from requests import Response


# class RemoveAgentTA:

#     @keyword
#     def remove_agent_api(self, uid: str):
#         url = f"https://qa.letsdochinese.com/userconfigserver/admin/update/user/teams"
#         headers = {
#         'Authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhY2FsaW1hZyIsImlhdCI6MTY5MTI0OTE2NX0.Nh6uj9uSOZD6nqz_KQ9D13Lbbl24mQE7fO3e3uazOVg",
#         'Content-Type': "application/json"
#     }

#         payload ={
#                 "uid": uid,
#                 "teamId": None
#             }
        

#         response = requests.put(url, headers=headers, data=json.dumps(payload))

#         # return response

#         if response.status_code == 200:
#             return response.json()
#         else:
#             return None
    


        