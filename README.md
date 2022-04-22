# BLE-Secutity-Tool

![](logo.jpg)

<p align="center"> <img src="https://img.shields.io/badge/Python-3.9-blue"> <img src="https://img.shields.io/badge/pip-bleak-blue"> <img src="https://img.shields.io/badge/Tested on-Kali 2022.1-green"></p>

写个小工具，我也不知道能写到什么程度Orz。

[可能因为bluez实现的某些问题](https://github.com/bluez/bluez/issues/219)，连接之后断开连接会报错。这时候可以重启一下蓝牙服务`service bluetooth restart`，然后拔插一下蓝牙适配器，这个问题完美的影响了工具运行的稳定性，会持续关注这个问题

# 目前实现的功能

- 扫描周围低功耗蓝牙设备
- 连接到低功耗蓝牙设备
- 扫描连接设备的服务
- 获取连接设备某服务的特性
- 读取某特性的值
- 向某特性写入值



