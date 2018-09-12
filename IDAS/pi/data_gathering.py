import serial
from IDAS import IDAS
import json
subscriptions={}


def check_id_subscription(ID):
	#Checkear si la subscription existe o no
	response = idas.getSubscriptionsIds(ID)
	print "esta es la respuesta"
	response_json = json.loads(response.text)
	print response_json
	try:
		response_json['errorCode']	
		value_ID =False
	except: 
		print("Entidad subscrita...")
		value_ID = True
	print 
	return value_ID



idas = IDAS()
print(idas.checkVersion())
while True:
	with serial.Serial('/dev/ttyACM0', 9600,timeout=2) as ser:
		#x = ser.read()          # read one byte
		#s = ser.read(10)        # read up to ten bytes (timeout)
		line = ser.readline()   # read a '\n' terminated line
		sensor1 = line.split()
		print(sensor1[0][0:len(sensor1[0])-1])
		response = idas.getEntityById(sensor1[0][0:len(sensor1[0])-1])
		response_json = json.loads(response.text)
		############################################### Creamos la entidad 1 #########################################
		try:
			response_json['contextResponses']
			print("Entidad Creada...")
		except:
			response_json['errorCode']['code'] == '404'
			print("Entidad no creada... Vamos a crearla...")
			#response = idascreateEntityWithOneAttribute(ENTITY_ID,ENTITY_TYPE,ENTITY_ATTR,ENTITY_ATTR_TYPE,ENTITY_ATTR_VALUE)
			response  = idas.createEntityWithOneAttribute(sensor1[0][0:len(sensor1[0])-1],'Sensor','Temperature','Celsios',sensor1[1])
		print(line)

        ################################################ Creamos la entidad 2 ################################3333#
		try:
			response_json['contextResponses']
			print("Entidad Creada...")
		except:
			response_json['errorCode']['code'] == '404'
			print("Entidad no creada... Vamos a crearla...")
			#response = idascreateEntityWithOneAttribute(ENTITY_ID,ENTITY_TYPE,ENTITY_ATTR,ENTITY_ATTR_TYPE,ENTITY_ATTR_VALUE)
			response  = idas.createEntityWithOneAttribute(sensor1[0][0:len(sensor1[0])-1],'Sensor','Temperature','Celsios',sensor1[1])
		print(line)
        

		############################# Registramos la entidad para realizar persistencia ################################
		#response
		#setSubscription(self,ENTITY_ID,ENTITY_ATTR,SERVER_URL):
		
		try: 
			subscriptions[sensor1[0][0:len(sensor1[0])-1]]
			print "Existe la subscripcion" + str(subscriptions[sensor1[0][0:len(sensor1[0])-1]])
		except:
			#no esta subscritot, hacemos subscritpion
			response =  idas.setSubscription(sensor1[0][0:len(sensor1[0])-1],'Temperature','http://192.168.0.49:5050/notify')
			response_JSON =json.loads(response.text)
			print (response_JSON)			
			subscriptions[sensor1[0][0:len(sensor1[0])-1]] = response_JSON['subscribeResponse']["subscriptionId"]
			#checkear si todo va bien
			#enviar informacion
			#updateEntityAttribute(self,ENTITY_ID,ENTITY_TYPE,ENTITY_ATTR,ENTITY_ATTR_TYPE,ENTITY_ATTR_VALUE):
		response = idas.updateEntityAttribute(sensor1[0][0:len(sensor1[0])-1],'Sensor','Temperature','Celsios',sensor1[1])


		


		#########################################Actualizamos los datos de la entidad ############################
		response = idas.updateEntityAttribute(sensor1[0][0:len(sensor1[0])-1],'Sensor','Temperature','Celsios',sensor1[1])





		################33333333###########################Finalmente, nos desconectamos######################################################
		line = ser.readline()   # read a '\n' terminated line
		sensor1 = line.split()
		print(sensor1[0][0:len(sensor1[0])-1])
		response = idas.getEntityById(sensor1[0][0:len(sensor1[0])-1])
		response_json = json.loads(response.text)
		############################################### Creamos la entidad 1 #########################################
		try:
			response_json['contextResponses']
			print("Entidad Creada...")
		except:
			response_json['errorCode']['code'] == '404'
			print("Entidad no creada... Vamos a crearla...")
			#response = idascreateEntityWithOneAttribute(ENTITY_ID,ENTITY_TYPE,ENTITY_ATTR,ENTITY_ATTR_TYPE,ENTITY_ATTR_VALUE)
			response  = idas.createEntityWithOneAttribute(sensor1[0][0:len(sensor1[0])-1],'Sensor','Temperature','Celsios',sensor1[1])
		print(line)
                line = ser.readline()

        ################################################ Creamos la entidad 2 ################################3333#
		try:
			response_json['contextResponses']
			print("Entidad Creada...")
		except:
			response_json['errorCode']['code'] == '404'
			print("Entidad no creada... Vamos a crearla...")
			#response = idascreateEntityWithOneAttribute(ENTITY_ID,ENTITY_TYPE,ENTITY_ATTR,ENTITY_ATTR_TYPE,ENTITY_ATTR_VALUE)
			response  = idas.createEntityWithOneAttribute(sensor1[0][0:len(sensor1[0])-1],'Sensor','Temperature','Celsios',sensor1[1])
		print(line)
		print(line)
		############################# Registramos la entidad para realizar persistencia ################################
		#response
		#setSubscription(self,ENTITY_ID,ENTITY_ATTR,SERVER_URL):
		try: 
			subscriptions[sensor1[0][0:len(sensor1[0])-1]]
			print "Existe la subscripcion" + str(subscriptions[sensor1[0][0:len(sensor1[0])-1]])
		except:
			#no esta subscritot, hacemos subscritpion
			response =  idas.setSubscription(sensor1[0][0:len(sensor1[0])-1],'Temperature','http://192.168.0.49:5050/notify')
			response_JSON =json.loads(response.text)
			print (response_JSON)			
			subscriptions[sensor1[0][0:len(sensor1[0])-1]] = response_JSON['subscribeResponse']["subscriptionId"]
			#checkear si todo va bien
			#enviar informacion
			#updateEntityAttribute(self,ENTITY_ID,ENTITY_TYPE,ENTITY_ATTR,ENTITY_ATTR_TYPE,ENTITY_ATTR_VALUE):
		response = idas.updateEntityAttribute(sensor1[0][0:len(sensor1[0])-1],'Sensor','Temperature','Celsios',sensor1[1])

		


		#########################################Actualizamos los datos de la entidad ############################
		response = idas.updateEntityAttribute(sensor1[0][0:len(sensor1[0])-1],'Sensor','Temperature','Celsios',sensor1[1])



