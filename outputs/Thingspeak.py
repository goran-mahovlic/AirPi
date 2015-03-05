#Pushing data to Thingspeak
# python

import output
import datetime
import httplib, urllib

class Print(output.Output):
	requiredData = []
	optionalData = []
	def __init__(self,data):
		pass
	def outputData(self,dataPoints):
    Data[]
		print ""
		print "Time: " + str(datetime.datetime.now())
		for i in dataPoints:
      Data[i] = str(i["value"])
			print i["name"] + ": " + str(i["value"]) + " " + i["symbol"]
		return True
    params = urllib.urlencode({'field1': Data[0], 'field2': Data[1],'field3': Data[2],'field4': Data[3], 'field5': Data[4],'field6': Data[5],'field7': Data[6],'field8': Data[7],'key':'34WTPBE2DXIESA5E'})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    conn.close()
