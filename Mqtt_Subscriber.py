import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code " + str(rc))
    client.subscribe("libin/livechat")

def on_message(client, userdata, msg):
    print(f"\n📩 Received: {msg.payload.decode()}")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()