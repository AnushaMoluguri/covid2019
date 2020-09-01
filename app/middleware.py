import requests
import json
class covid19Middleware():
    def __init__(self,get_response):
        self.get_response=get_response
        print("I am contractor")
        response=requests.get("https://api.covid19india.org/state_district_wise.json")
        print(response.status_code)
        dict_data=json.loads(response.text)
        s=json.dump(dict_data,open("app/raw/covid19.json","w"))

        print("data was written into file")

    def __call__(self,request, *args, **kwargs):
        response=self.get_response(request)
        print("I am call")
        return response