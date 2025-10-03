import paho.mqtt.client as mqtt

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()

while True:
    message = input("📤 Enter message to send: ")
    if message.lower() == "exit":
        break
    client.publish("libin/livechat", message)

client.loop_stop()
client.disconnect()