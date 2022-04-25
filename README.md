# BLE-Security-Tool

![](logo.jpg)

<p align="center"> <img src="https://img.shields.io/badge/Python-3.9-blue"> <img src="https://img.shields.io/badge/pip-bleak-blue"> <img src="https://img.shields.io/badge/Tested on-Kali 2022.1-green"></p>
写个小工具，我也不知道能写到什么程度Orz。

[可能因为bluez实现的某些问题](https://github.com/bluez/bluez/issues/219)，连接之后断开连接会报错。这时候可以重启一下蓝牙服务`service bluetooth restart`，然后拔插一下蓝牙适配器，这个问题完美的影响了工具运行的稳定性

还有个问题，目前bleak只能用hci0来连接啥的，但是很多时候机器上的适配器编号是hci1啥的，这时候就会报错，[参考](https://github.com/hbldh/bleak/issues/513)，目前扫描蓝牙设备是可以指定适配器的，已经在代码中加上了

# 目前实现的功能

- 扫描周围低功耗蓝牙设备
- 连接到低功耗蓝牙设备
- 扫描连接设备的服务
- 获取连接设备某服务的特征
- 读取某特征的值
- 向某特征写入值
- 方向键上下选择之前输入的命令
- 监听特征的通知和指示



