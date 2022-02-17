import json
import requests
import xmltodict
import asyncio
from hikvisionapi.hikvisionapi import response_parser
from httpcore.backends import asyncio
from requests.auth import HTTPDigestAuth
class Vehicle():
       url_cam_plate = 'http://186.69.152.58:81/ISAPI/Traffic/channels/1/vehicleDetect/plates'
       response = requests.post(
                           url=url_cam_plate,
                           stream=True,
                           auth=HTTPDigestAuth(
                               'admin',
                               'Asd12345'
                               ),

                           data='<AfterTime><picTime>2020-03-07T21:00:00Z</picTime></AfterTime>'
                              )
       def getlastplate(self):
           print(self.response.text)
           print(response_parser(self.response))
           plate = self.response_parser(self.response)['Plates']['Plate'][-1]['plateNumber']
           return plate

       def response_parser(self,response, present='dict'):
           if isinstance(response, (list,)):
               result = "".join(response)
           else:
               result = response.text

           if present == 'dict':
               if isinstance(response, (list,)):
                   events = []
                   for event in response:
                       e = json.loads(json.dumps(xmltodict.parse(event)))
                       events.append(e)
                   return events
               return json.loads(json.dumps(xmltodict.parse(result)))
           else:
               return result
car=Vehicle();
print(car.getlastplate())
