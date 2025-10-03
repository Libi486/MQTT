How to Test
Open two terminal windows.
Run subscriber.py in one window.
Run publisher.py in the other.
You should see the message appear in the subscriber window.

Things to Install
pip install paho-mqtt

✅ Setup Overview
One script will act as the Subscriber – always listening for messages.
Another script will act as the Publisher – you’ll run it manually to send messages.
Both will use a public MQTT broker (HiveMQ) so you don’t need to install anything extra.


🧠 What is MQTT?
MQTT (Message Queuing Telemetry Transport) is a lightweight, publish-subscribe 
network protocol designed for fast, reliable communication between devices — especially in IoT (Internet of Things) environments.

⚙️ How MQTT Works
1. Broker
Acts as a central hub.
Receives all messages and routes them to the correct subscribers.
Examples: Mosquitto, HiveMQ, EMQX.
2. Publisher
Sends messages to a topic.
Doesn’t care who receives the message.
3. Subscriber
Listens to a topic.
Receives messages published to that topic.

🔁 Communication Flow
Publisher → MQTT Broker → Subscriber

📦 MQTT Message Structure
Topic: A string like home/livingroom/temperature.
Payload: The actual message (e.g., "22.5°C").
QoS (Quality of Service):

0: At most once (no guarantee).
1: At least once (may be duplicated).
2: Exactly once (most reliable).

🧪 Why Use MQTT?
Lightweight and fast.
Ideal for low-bandwidth or unreliable networks.
Works well for real-time communication.
Easy to implement in Python, Node.js, C++, etc.
