import requests, json, re 
import ConfigParser
import io
import sys
from collections import Counter
import SocketServer, sys, os, time


class IDAS(object):
	def __init__(self):
		print "Object created"

	def cancelSubscriptionById(self,SUBSCRIPTION_ID):
		CONFIG_FILE = "config.ini"

		# Load the configuration file
		with open(CONFIG_FILE,'r+') as f:
		    sample_config = f.read()
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.readfp(io.BytesIO(sample_config))

		CB_HOST=config.get('contextbroker', 'host')
		CB_PORT=config.get('contextbroker', 'port')
		CB_FIWARE_SERVICE=config.get('contextbroker', 'fiware_service')
		CB_FIWARE_SERVICEPATH=config.get('contextbroker', 'fiware-service-path')
		CB_AAA=config.get('contextbroker', 'OAuth')
		if CB_AAA == "yes":
		    TOKEN=config.get('user', 'token')
		    TOKEN_SHOW=TOKEN[1:5]+"**********************************************************************"+TOKEN[-5:]
		else:
		    TOKEN="NULL"
		    TOKEN_SHOW="NULL"

		NODE_ID=config.get('local', 'host_id')
		f.close()

		CB_URL = "http://"+CB_HOST+":"+CB_PORT

		PAYLOAD = '{ \
		  "subscriptionId": "'+SUBSCRIPTION_ID+'" \
		}'

		HEADERS = {'content-type': 'application/json','accept': 'application/json', 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}
		HEADERS_SHOW = {'content-type': 'application/json', 'accept': 'application/json' , 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH , 'X-Auth-Token' : TOKEN_SHOW}

		URL = CB_URL + '/v1/unsubscribeContext'

		print "* Asking to "+URL
		print "* Headers: "+str(HEADERS_SHOW)
		print "* Sending PAYLOAD: "
		print json.dumps(json.loads(PAYLOAD), indent=4)
		print
		print "..."
		r = requests.post(URL, data=PAYLOAD, headers=HEADERS)
		print
		print "* Status Code: "+str(r.status_code)
		print
		print r.text
		print
		return r

	def getEntityById(self,ENTITY_ID):
		CONFIG_FILE = "config.ini"

		# Load the configuration file
		with open(CONFIG_FILE,'r+') as f:
		    sample_config = f.read()
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.readfp(io.BytesIO(sample_config))

		CB_HOST=config.get('contextbroker', 'host')
		CB_PORT=config.get('contextbroker', 'port')
		CB_FIWARE_SERVICE=config.get('contextbroker', 'fiware_service')
		CB_AAA=config.get('contextbroker', 'OAuth')
		if CB_AAA == "yes":
		    TOKEN=config.get('user', 'token')
		    TOKEN_SHOW=TOKEN[1:5]+"**********************************************************************"+TOKEN[-5:]
		else:
		    TOKEN="NULL"
		    TOKEN_SHOW="NULL"

		CB_URL = "http://"+CB_HOST+":"+CB_PORT
		HEADERS = {'content-type': 'application/json' , 'accept': 'application/json', 'Fiware-Service': CB_FIWARE_SERVICE, 'X-Auth-Token' : TOKEN}
		HEADERS_SHOW = {'content-type': 'application/json', 'accept': 'application/json' , 'Fiware-Service': CB_FIWARE_SERVICE, 'X-Auth-Token' : TOKEN_SHOW}
		PAYLOAD = '{                \
		    "entities": [           \
		    {                        \
		        "type": "",   \
		        "isPattern": "false", \
		        "id": "'+ENTITY_ID+'"  \
		    }  \
		    ],  \
		    "attributes" : [ ] \
		}'

		URL = CB_URL + '/ngsi10/queryContext'

		print "* Asking to "+URL
		print "* Headers: "+str(HEADERS_SHOW)
		print "* Sending PAYLOAD: "
		print json.dumps(json.loads(PAYLOAD), indent=4)
		print
		print "..."
		r = requests.post(URL, data=PAYLOAD, headers=HEADERS)
		print
		print "* Status Code: "+str(r.status_code)
		print "* Response: "
		print r.text
		print
		return r


	def checkVersion(self):
		CONFIG_FILE = "config.ini"
		# Load the configuration file
		with open(CONFIG_FILE,'r+') as f:
		    sample_config = f.read()
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.readfp(io.BytesIO(sample_config))

		CB_HOST=config.get('contextbroker', 'host')
		CB_PORT=config.get('contextbroker', 'port')
		CB_AAA=config.get('contextbroker', 'OAuth')

		if CB_AAA == "yes":
		    TOKEN=config.get('user', 'token')
		    TOKEN_SHOW=TOKEN[1:5]+"**********************************************************************"+TOKEN[-5:]
		else:
		    TOKEN="NULL"
		    TOKEN_SHOW="NULL"    

		NODE_ID=config.get('local', 'host_id')
		f.close()

		CB_URL = "http://"+CB_HOST+":"+CB_PORT
		PAYLOAD = {'some' : 'data'}
		HEADERS = {'Content-Type': 'application/json' ,'accept': 'application/json','X-Auth-Token' : TOKEN}
		HEADERS_SHOW = {'Content-Type': 'application/json' ,'accept': 'application/json' , 'X-Auth-Token' : TOKEN_SHOW}

		URL = CB_URL + '/version'

		print "* Asking to "+URL
		print "* Headers: "+str(HEADERS_SHOW)
		print "..."
		r = requests.get(URL, headers=HEADERS)
		print
		print "* Status Code: "+str(r.status_code)
		print "* Response: "
		print r.text
		print
		return r

	def createEntityWithOneAttribute(self,ENTITY_ID,ENTITY_TYPE,ENTITY_ATTR,ENTITY_ATTR_TYPE,ENTITY_ATTR_VALUE):
		CONFIG_FILE = "config.ini"

		# Load the configuration file
		with open(CONFIG_FILE,'r+') as f:
		    sample_config = f.read()
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.readfp(io.BytesIO(sample_config))

		CB_HOST=config.get('contextbroker', 'host')
		CB_PORT=config.get('contextbroker', 'port')
		CB_FIWARE_SERVICE=config.get('contextbroker', 'fiware_service')
		CB_FIWARE_SERVICEPATH=config.get('contextbroker', 'fiware-service-path')
		CB_AAA=config.get('contextbroker', 'OAuth')
		if CB_AAA == "yes":
		    TOKEN=config.get('user', 'token')
		    TOKEN_SHOW=TOKEN[1:5]+"**********************************************************************"+TOKEN[-5:]
		else:
		    TOKEN="NULL"
		    TOKEN_SHOW="NULL"

		CB_URL = "http://"+CB_HOST+":"+CB_PORT
		HEADERS = {'content-type': 'application/json','accept': 'application/json', 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}
		HEADERS_SHOW = {'content-type': 'application/json', 'accept': 'application/json' , 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH , 'X-Auth-Token' : TOKEN_SHOW}

		PAYLOAD = '{ \
		    "contextElements": [ \
		        { \
		            "type": "'+ENTITY_TYPE+'", \
		            "isPattern": "false",  \
		            "id": "'+ENTITY_ID+'", \
		            "attributes": [ \
		            { \
		                "name": "'+ENTITY_ATTR+'",  \
		                "type": "'+ENTITY_ATTR_TYPE+'", \
		                "value": "'+ENTITY_ATTR_VALUE+'" \
		            } \
		            ] \
		        } \
		    ], \
		    "updateAction": "APPEND" \
		}'

		URL = CB_URL + '/v1/updateContext'

		print "* Asking to "+URL
		print "* Headers: "+str(HEADERS_SHOW)
		print "* Sending PAYLOAD: "
		print json.dumps(json.loads(PAYLOAD), indent=4)
		print
		print "..."
		r = requests.post(URL, data=PAYLOAD, headers=HEADERS)
		print
		print "* Status Code: "+str(r.status_code)
		print "* Response: "
		print r.text
		print
		return r

	def deleteEntityByIdAndType(self,ENTITY_ID,ENTITY_TYPE):
		CONFIG_FILE = "config.ini"

		# Load the configuration file
		with open(CONFIG_FILE,'r+') as f:
		    sample_config = f.read()
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.readfp(io.BytesIO(sample_config))

		CB_HOST=config.get('contextbroker', 'host')
		CB_PORT=config.get('contextbroker', 'port')
		CB_FIWARE_SERVICE=config.get('contextbroker', 'fiware_service')
		CB_FIWARE_SERVICEPATH=config.get('contextbroker', 'fiware-service-path')
		CB_AAA=config.get('contextbroker', 'OAuth')
		if CB_AAA == "yes":
		    TOKEN=config.get('user', 'token')
		    TOKEN_SHOW=TOKEN[1:5]+"**********************************************************************"+TOKEN[-5:]
		else:
		    TOKEN="NULL"
		    TOKEN_SHOW="NULL"

		CB_URL = "http://"+CB_HOST+":"+CB_PORT
		HEADERS = {'content-type': 'application/json','accept': 'application/json', 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}
		HEADERS_SHOW = {'content-type': 'application/json', 'accept': 'application/json' , 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH , 'X-Auth-Token' : TOKEN_SHOW}

		PAYLOAD = '{ \
		    "contextElements": [ \
		        { \
		            "type": "'+ENTITY_TYPE+'", \
		            "isPattern": "false",  \
		            "id": "'+ENTITY_ID+'" \
		        } \
		    ], \
		    "updateAction": "DELETE" \
		}'

		URL = CB_URL + '/v1/updateContext'

		print "* Asking to "+URL
		print "* Headers: "+str(HEADERS_SHOW)
		print "* Sending PAYLOAD: "
		print json.dumps(json.loads(PAYLOAD), indent=4)
		print
		print "..."
		r = requests.post(URL, data=PAYLOAD, headers=HEADERS)
		print
		print "* Status Code: "+str(r.status_code)
		print "* Response: "
		print r.text
		print
		return r

	def GetEntitiesByType(self,ENTITY_TYPE):
		CONFIG_FILE = "config.ini"
		if ENTITY_TYPE == "ALL":
		    ENTITY_TYPE = ""

		# Load the configuration file
		with open(CONFIG_FILE,'r+') as f:
		    sample_config = f.read()
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.readfp(io.BytesIO(sample_config))

		CB_HOST=config.get('contextbroker', 'host')
		CB_PORT=config.get('contextbroker', 'port')
		CB_FIWARE_SERVICE=config.get('contextbroker', 'fiware_service')
		CB_FIWARE_SERVICEPATH=config.get('contextbroker', 'fiware-service-path')
		CB_AAA=config.get('contextbroker', 'OAuth')
		if CB_AAA == "yes":
		    TOKEN=config.get('user', 'token')
		    TOKEN_SHOW=TOKEN[1:5]+"**********************************************************************"+TOKEN[-5:]
		else:
		    TOKEN="NULL"
		    TOKEN_SHOW="NULL"

		NODE_ID=config.get('local', 'host_id')
		f.close()

		CB_URL = "http://"+CB_HOST+":"+CB_PORT
		PAYLOAD = '{                \
		    "entities": [           \
		    {                        \
		        "type": "'+ENTITY_TYPE+'",   \
		        "isPattern": "true", \
		        "id": ".*"  \
		    }  \
		    ],  \
		    "attributes" : [ ] \
		}'

		HEADERS = {'content-type': 'application/json','accept': 'application/xml', 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}
		HEADERS_SHOW = {'content-type': 'application/json', 'accept': 'application/xml' , 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH , 'X-Auth-Token' : TOKEN_SHOW}

		URL = CB_URL + '/ngsi10/queryContext'

		print "* Asking to "+URL
		print "* Headers: "+str(HEADERS_SHOW)
		print "* Sending PAYLOAD: "
		print json.dumps(json.loads(PAYLOAD), indent=4)
		print
		print "..."
		r = requests.post(URL, data=PAYLOAD, headers=HEADERS)
		print
		print "* Status Code: "+str(r.status_code)

		list_id = re.findall(r'<id>[\w]*.', r.text)
		list_type = re.findall('<entityId type=\S+ isPattern=\S+>', r.text)
		Num_id=len(list_id)
		Num_type=len(list_type)
		cnt_id=Counter(list_id)
		cnt_type=Counter(list_type)

		print "***** Number of Entity Types: "+str(Num_type)
		print
		print "***** List of Entity Types"
		for x in cnt_type.most_common():
		    print '%s : %d' % x
		print
		print "**** Number of Entity IDs: "+str(Num_id)
		print
		print "**** List of Entity IDs"
		for x in cnt_id.most_common():
		    print '%s : %d' % x
		print

		ASK = str(raw_input("Do you want me to print all Entities? (yes/no)"))
		if ASK == "yes":
		    print r.text

		print
		return r

	def getEntityAttribute(self,ENTITY_ID,ENTITY_ATTR):
		CONFIG_FILE = "config.ini"

		# Load the configuration file
		with open(CONFIG_FILE,'r+') as f:
		    sample_config = f.read()
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.readfp(io.BytesIO(sample_config))

		CB_HOST=config.get('contextbroker', 'host')
		CB_PORT=config.get('contextbroker', 'port')
		CB_FIWARE_SERVICE=config.get('contextbroker', 'fiware_service')
		CB_FIWARE_SERVICEPATH=config.get('contextbroker', 'fiware-service-path')

		CB_AAA=config.get('contextbroker', 'OAuth')
		if CB_AAA == "yes":
		    TOKEN=config.get('user', 'token')
		    TOKEN_SHOW=TOKEN[1:5]+"**********************************************************************"+TOKEN[-5:]
		else:
		    TOKEN="NULL"
		    TOKEN_SHOW="NULL"

		CB_URL = "http://"+CB_HOST+":"+CB_PORT
		HEADERS = {'content-type': 'application/json','accept': 'application/json', 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}
		HEADERS_SHOW = {'content-type': 'application/json', 'accept': 'application/json' , 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH , 'X-Auth-Token' : TOKEN_SHOW}

		PAYLOAD = '{                \
		    "entities": [           \
		    {                        \
		        "type": "",   \
		        "isPattern": "false", \
		        "id": "'+ENTITY_ID+'"  \
		    }  \
		    ],  \
		    "attributes" : ["'+ENTITY_ATTR+'"] \
		}'

		URL = CB_URL + '/ngsi10/queryContext'

		print "* Asking to "+URL
		print "* Headers: "+str(HEADERS_SHOW)
		print "* Sending PAYLOAD: "
		print json.dumps(json.loads(PAYLOAD), indent=4)
		print
		print "..."
		r = requests.post(URL, data=PAYLOAD, headers=HEADERS)
		print
		print "* Status Code: "+str(r.status_code)
		print "* Response: "
		print r.text
		print
		return r

	def setSubscription(self,ENTITY_ID,ENTITY_ATTR,SERVER_URL):
		CONFIG_FILE = "config.ini"
		
		# Load the configuration file
		with open(CONFIG_FILE,'r+') as f:
		    sample_config = f.read()
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.readfp(io.BytesIO(sample_config))

		CB_HOST=config.get('contextbroker', 'host')
		CB_PORT=config.get('contextbroker', 'port')
		CB_FIWARE_SERVICE=config.get('contextbroker', 'fiware_service')
		CB_FIWARE_SERVICEPATH=config.get('contextbroker', 'fiware-service-path')

		CB_AAA=config.get('contextbroker', 'OAuth')
		if CB_AAA == "yes":
		    TOKEN=config.get('user', 'token')
		    TOKEN_SHOW=TOKEN[1:5]+"**********************************************************************"+TOKEN[-5:]
		else:
		    TOKEN="NULL"
		    TOKEN_SHOW="NULL"

		NODE_ID=config.get('local', 'host_id')
		f.close()

		CB_URL = "http://"+CB_HOST+":"+CB_PORT

		MIN_INTERVAL = "PT5S"
		DURATION = "P1M"
		ENTITY_TYPE = ""
		ENTITY_ATTR_WATCH = ENTITY_ATTR
		ENTITY_ATTR_NOTIFY = ENTITY_ATTR

		PAYLOAD = '{ \
		    "entities": [ \
		        { \
		            "type": "'+ENTITY_TYPE+'", \
		            "isPattern": "false", \
		            "id": "'+ENTITY_ID+'" \
		        } \
		    ], \
		    "attributes": [ \
		        "'+ENTITY_ATTR_NOTIFY+'" \
		    ], \
		    "reference": "'+SERVER_URL+'", \
		    "duration": "'+DURATION+'", \
		    "notifyConditions": [ \
		        { \
		            "type": "ONCHANGE", \
		            "condValues": [ \
		                "'+ENTITY_ATTR_WATCH+'" \
		            ] \
		        } \
		    ], \
		    "throttling": "'+MIN_INTERVAL+'" \
		}' 

		HEADERS = {'content-type': 'application/json','accept': 'application/json', 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}
		HEADERS_SHOW = {'content-type': 'application/json', 'accept': 'application/json' , 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH , 'X-Auth-Token' : TOKEN_SHOW}

		URL = CB_URL + '/v1/subscribeContext'

		print "* Asking to "+URL
		print "* Headers: "+str(HEADERS_SHOW)
		print "* Sending PAYLOAD: "
		print json.dumps(json.loads(PAYLOAD), indent=4)
		print
		print "..."
		r = requests.post(URL, data=PAYLOAD, headers=HEADERS)
		print
		print "* Status Code: "+str(r.status_code)
		print
		print r.text
		print
		return r

	def subscriptionDaemon(self,SERVER_PORT,HANDLING_SCRIPT):
		SERVER_OK_RESPONSE = {'return':'ok'}

		# Use this for only-IPv4 incoming connections 
		SERVER_ADDRESS='127.0.0.1'

		# User this one for IPv4 or IPv6 connections.
		# IMPORTANT: For this to work in Python 2.7 you need to edit "/usr/lib/python2.7/SocketServer.py" file
		#               Change "address_family = socket.AF_INET" line by "address_family = socket.AF_INET6".
		#            This is because SocketServer is buggy on this. Check this out at: http://bugs.python.org/issue20215 
		#            For Python 3.5 there is a patch available at the link above.

		#SERVER_ADDRESS='::'

		class MyTCPServer(SocketServer.ThreadingTCPServer):
		    allow_reuse_address = True

		class MyTCPServerHandler(SocketServer.BaseRequestHandler):
		    def handle(self):
		        try:
		            data = json.loads(self.request.recv(1024).strip())
		            # process the received data
		            EXEC_FILE = 'python '+HANDLING_SCRIPT+' "'+str(data)+'"'
		            localtime = time.asctime( time.localtime(time.time()) )
		            print localtime+" - SubscriptionDaemon.py calling: ", EXEC_FILE
		            os.system(EXEC_FILE)
		            # send 'ok' back to client
		            self.request.sendall(json.dumps(SERVER_OK_RESPONSE))
		        except Exception, e:
		            localtime = time.asctime( time.localtime(time.time()) )
		            print localtime+" - Exception while receiving message: ", e

		server = MyTCPServer((SERVER_ADDRESS, SERVER_PORT), MyTCPServerHandler)
		server.serve_forever()

	def testDaemon(self,SERVER_PORT):
		data = {'message':'hello world!', 'test':123.4}

		# Use this for IPv4
		SERVER_ADDRESS = '127.0.0.1'
		ADDRESS_FAMILY = 'AF_INET'

		# Use this if your server is listening IPv6 connections.
		#SERVER_ADDRESS = '::1'
		#ADDRESS_FAMILY = 'AF_INET6'

		SOCKET_FAMILY = 'socket.'+ADDRESS_FAMILY
		SOCKET_TYPE = 'socket.SOCK_STREAM'
		s = socket.socket(eval(SOCKET_FAMILY), eval(SOCKET_TYPE))
		s.connect((SERVER_ADDRESS, SERVER_PORT))
		s.send(json.dumps(data))
		result = json.loads(s.recv(1024))
		print result
		s.close()

	def updateEntityAttribute(self,ENTITY_ID,ENTITY_TYPE,ENTITY_ATTR,ENTITY_ATTR_TYPE,ENTITY_ATTR_VALUE):
		CONFIG_FILE = "config.ini"

		# Load the configuration file
		with open(CONFIG_FILE,'r+') as f:
		    sample_config = f.read()
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.readfp(io.BytesIO(sample_config))

		CB_HOST=config.get('contextbroker', 'host')
		CB_PORT=config.get('contextbroker', 'port')
		CB_FIWARE_SERVICE=config.get('contextbroker', 'fiware_service')
		CB_FIWARE_SERVICEPATH=config.get('contextbroker', 'fiware-service-path')
		CB_AAA=config.get('contextbroker', 'OAuth')
		if CB_AAA == "yes":
		    TOKEN=config.get('user', 'token')
		    TOKEN_SHOW=TOKEN[1:5]+"**********************************************************************"+TOKEN[-5:]
		else:
		    TOKEN="NULL"
		    TOKEN_SHOW="NULL"

		CB_URL = "http://"+CB_HOST+":"+CB_PORT
		HEADERS = {'content-type': 'application/json','accept': 'application/json', 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}
		HEADERS_SHOW = {'content-type': 'application/json', 'accept': 'application/json' , 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH , 'X-Auth-Token' : TOKEN_SHOW}

		PAYLOAD = '{ \
		    "contextElements": [ \
		        { \
		            "type": "'+ENTITY_TYPE+'", \
		            "isPattern": "false",  \
		            "id": "'+ENTITY_ID+'", \
		            "attributes": [ \
		            { \
		                "name": "'+ENTITY_ATTR+'",  \
		                "type": "'+ENTITY_ATTR_TYPE+'", \
		                "value": "'+ENTITY_ATTR_VALUE+'" \
		            } \
		            ] \
		        } \
		    ], \
		    "updateAction": "UPDATE" \
		}'

		URL = CB_URL + '/v1/updateContext'

		print "* Asking to "+URL
		print "* Headers: "+str(HEADERS_SHOW)
		print "* Sending PAYLOAD: "
		print json.dumps(json.loads(PAYLOAD), indent=4)
		print
		print "..."
		r = requests.post(URL, data=PAYLOAD, headers=HEADERS)
		print
		print "* Status Code: "+str(r.status_code)
		print "* Response: "
		print r.text
		print
		return r

	def getSubscriptionsIds(self,subscriptionId):
		CONFIG_FILE = "config.ini"

		# Load the configuration file
		with open(CONFIG_FILE,'r+') as f:
		    sample_config = f.read()
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.readfp(io.BytesIO(sample_config))

		CB_HOST=config.get('contextbroker', 'host')
		CB_PORT=config.get('contextbroker', 'port')
		CB_FIWARE_SERVICE=config.get('contextbroker', 'fiware_service')
		CB_FIWARE_SERVICEPATH=config.get('contextbroker', 'fiware-service-path')

		CB_AAA=config.get('contextbroker', 'OAuth')
		if CB_AAA == "yes":
		    TOKEN=config.get('user', 'token')
		    TOKEN_SHOW=TOKEN[1:5]+"**********************************************************************"+TOKEN[-5:]
		else:
		    TOKEN="NULL"
		    TOKEN_SHOW="NULL"

		CB_URL = "http://"+CB_HOST+":"+CB_PORT
		HEADERS = {'content-type': 'application/json','accept': 'application/json', 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}
		HEADERS_SHOW = {'content-type': 'application/json', 'accept': 'application/json' , 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH , 'X-Auth-Token' : TOKEN_SHOW}

		PAYLOAD = '{ \
		    "subscriptionId": "'+subscriptionId+'" \
		}'

		URL = CB_URL + '/v1/SubscribeContext'

		print "* Asking to "+URL
		print "* Headers: "+str(HEADERS_SHOW)
		print "* Sending PAYLOAD: "
		print json.dumps(json.loads(PAYLOAD), indent=4)
		print
		print "..."
		r = requests.post(URL, data=PAYLOAD, headers=HEADERS)
		print
		print "* Status Code: "+str(r.status_code)
		print "* Response: "
		print r.text
		print
		return r

	def check_subscriptions_V2(self):
		CONFIG_FILE = "config.ini"

		# Load the configuration file
		with open(CONFIG_FILE,'r+') as f:
		    sample_config = f.read()
		config = ConfigParser.RawConfigParser(allow_no_value=True)
		config.readfp(io.BytesIO(sample_config))

		CB_HOST=config.get('contextbroker', 'host')
		CB_PORT=config.get('contextbroker', 'port')
		CB_FIWARE_SERVICE=config.get('contextbroker', 'fiware_service')
		CB_FIWARE_SERVICEPATH=config.get('contextbroker', 'fiware-service-path')

		CB_AAA=config.get('contextbroker', 'OAuth')
		if CB_AAA == "yes":
		    TOKEN=config.get('user', 'token')
		    TOKEN_SHOW=TOKEN[1:5]+"**********************************************************************"+TOKEN[-5:]
		else:
		    TOKEN="NULL"
		    TOKEN_SHOW="NULL"

		CB_URL = "http://"+CB_HOST+":"+CB_PORT
		HEADERS = {'content-type': 'application/json','accept': 'application/json', 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH,'X-Auth-Token' : TOKEN}
		HEADERS_SHOW = {'content-type': 'application/json', 'accept': 'application/json' , 'Fiware-Service': CB_FIWARE_SERVICE ,'Fiware-ServicePath': CB_FIWARE_SERVICEPATH , 'X-Auth-Token' : TOKEN_SHOW}

		PAYLOAD = '{ \
		    "subscriptionId": "'+subscriptionId+'" \
		}'

		URL = CB_URL + '/v2/subscriptions'

		print "* Asking to "+URL
		print "* Headers: "+str(HEADERS_SHOW)
		print "* Sending PAYLOAD: "
		print json.dumps(json.loads(PAYLOAD), indent=4)
		print
		print "..."
		r = requests.post(URL, data=PAYLOAD, headers=HEADERS)
		print
		print "* Status Code: "+str(r.status_code)
		print "* Response: "
		print r.text
		print
		return r
		