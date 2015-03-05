#Pushing data to Thingspeak
# python

import output
import datetime
import httplib, urllib

class ThingSpeak(output.Output):
    requiredData = ["APIKey"]
    optionalData = []
    def __init__(self,data):
        self.APIKey=data["APIKey"]
    def outputData(self,dataPoints):
        Data = ["1","2","3","4","5","6","7"]
        j = 0
	for i in dataPoints:
            Data[j] = str(i["value"])
            j = j + 1
        params = urllib.urlencode({'field1': Data[0], 'field2': Data[1],'field3': Data[2],'field4': Data[3], 'field5': Data[4] 'field6': Data[5],'field7': Data[6],'key':self.APIKey})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()
	return True
