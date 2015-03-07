import OSC
import time, random
client = OSC.OSCClient()
client.connect( ( '127.0.0.1', 57120 ) )
msg = OSC.OSCMessage()
msg.setAddress("/print")
msg.append(500)
client.send(msg)

while True:
	time.sleep(random.randint(1,3))
	msg[0] = random.randint(20, 1000)
	client.send(msg)