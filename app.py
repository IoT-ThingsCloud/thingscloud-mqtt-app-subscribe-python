# https://github.com/eclipse-paho/paho.mqtt.python
import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import json
import ssl

# 填写 MQTT 应用端订阅参数，在控制台获取
# 参考文档：https://www.thingscloud.xyz/docs/guide/api/project-mqtt-subscribe.html
# 只需填写以下 3 个参数，其它代码无需修改，即可运行
# (1) MQTT 地址
mqtt_url = "wss://..."
# (2) ProjectViewKey
project_view_key = ""
# (3) ProjectViewSecret
project_view_secret = ""

# 解析 MQTT 地址
parsed_url = urlparse(mqtt_url)
mqtt_host = parsed_url.hostname
mqtt_path = parsed_url.path

# 回调函数，当客户端连接到服务器时调用
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to ThingsCloud MQTT App Broker!")
        # 参考 ThingsCloud MQTT 应用端订阅文档，订阅需要的主题，可以订阅多个主题。
        # 注意：qos必须为0。
        client.subscribe(f"{project_view_key}/+/attributes", qos=0)
    else:
        print(f"Connection failed with code {rc}")

# 回调函数，当接收到消息时调用
def on_message(client, userdata, msg):
    try:
        # 解码消息并解析JSON
        payload = msg.payload.decode("utf-8")
        json_data = json.loads(payload)
        print(f"Received from [{msg.topic}]:")
        print(json.dumps(json_data, indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print(f"Invalid JSON received: {payload}")
    except Exception as e:
        print(f"Error processing message: {str(e)}")


# 创建 MQTT 客户端实例
client = mqtt.Client(transport="websockets", protocol=mqtt.MQTTv311)

# 配置 WebSocket 连接参数
client.ws_set_options(path=mqtt_path, headers=None)

# 配置 TLS 加密参数
client.tls_set(
    ca_certs="./ca_certs/iot-api.com_rsa_root.crt",  # 指定平台的 CA 根证书
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLS,
)

# 设置认证信息
client.username_pw_set(project_view_key, project_view_secret)

# 绑定回调函数
client.on_connect = on_connect
client.on_message = on_message

# 连接WSS Broker（端口通常为443）
client.connect(mqtt_host, 443, 600)

# 启动网络循环
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Disconnecting...")
    client.disconnect()
