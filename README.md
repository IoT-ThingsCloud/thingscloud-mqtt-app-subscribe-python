# ThingsCloud MQTT 应用端订阅 Python 示例

该示例代码展示了如何使用 ThingsCloud MQTT 应用端订阅服务，通过 Python 语言实现订阅设备消息的功能。


## 什么是 MQTT 应用端订阅

ThingsCloud 支持开放的 MQTT 应用端订阅服务，帮助您在自有软件应用或第三方应用中实时接收设备的最新消息。

您不仅可以在服务器上订阅设备消息，也可以在基于浏览器的 Web 应用中通过 Javascript 和 MQTT@Websocket 直接订阅设备实时消息，来实现 Web 页面实时更新设备数据，这在开发物联网数据可视化界面时发挥重要的作用。

详细介绍请参考 [MQTT 应用端订阅](https://www.thingscloud.xyz/docs/guide/api/project-mqtt-subscribe.html)。

## 如何运行示例代码

### 安装 Python

使用 Python 3.6 或以上版本。

### 安装 paho-mqtt 库

```
pip install paho-mqtt
```

### 下载示例代码

Clone 或下载该代码仓库，进入代码目录。

### 填写配置信息

进入 [ThingsCloud 控制台](https://console.thingscloud.xyz/)，在 **项目 > MQTT 应用端订阅** 中找到以下参数，填写在示例代码中。

- `mqtt_url`：MQTT 地址。
- `project_view_key`：ProjectViewKey
- `project_view_secret`：ProjectViewSecret


### 运行示例代码

```
python app.py
```

程序运行后，如果填写的参数正确，将提示已成功连接到平台。

![articles/2024/20250403090010_7807af28fee18c1bbd5319281245e1ad.png](https://img-1300291923.cos.ap-beijing.myqcloud.com/articles/2024/20250403090010_7807af28fee18c1bbd5319281245e1ad.png)

示例中订阅了所有设备的属性更新消息，您也可以根据实际需求修改订阅的主题。

![articles/2024/20250403090051_af203a79fa61f741e8f5ebe29fabab1f.png](https://img-1300291923.cos.ap-beijing.myqcloud.com/articles/2024/20250403090051_af203a79fa61f741e8f5ebe29fabab1f.png)
