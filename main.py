from prettytable import PrettyTable
from bleak import BleakScanner,BleakClient
from color import *
import sys,getopt,asyncio,os
from pyfiglet import Figlet

##################################################################

async def connclient(address):
    client = BleakClient(address)
    await client.connect()
    return client

async def disconnclient(client):
    await client.disconnect()

async def scan_devices():
    devices = await BleakScanner.discover()
    BLEdevices = PrettyTable([blue("编号"), yellow("设备地址"), green("设备名"), green("RSSI"), green("类型")])
    for i in range(0,len(devices)):
        BLEdevices.add_row([blue(str(i)), yellow(devices[i].address), green(devices[i].name),  green(str(devices[i].rssi)), green(str(devices[i].details["props"]["AddressType"]))])
    print(BLEdevices)

async def scan_services(client):
    SvcS = PrettyTable([blue("服务UUID"), yellow("句柄")])
    svcs = await client.get_services()
    for service in svcs:
        SvcS.add_row([blue(service.uuid),yellow(str(hex(service.handle)))])
    print(SvcS)

async def scan_characteristics(client,serviceid):
    CharS = PrettyTable([blue("特性UUID"), yellow("句柄"), green("属性")])
    svcs = await client.get_services()
    for service in svcs:
        if service.uuid == serviceid:
            for char in service.characteristics:
                CharS.add_row([blue(char.uuid),yellow(str(hex(char.handle))),green('; '.join(char.properties))])
        else:
            pass
    CharS.align[green("属性")] = 'l'
    print(CharS)

async def read_value(address,charuuid):
    try:
        value = bytes(await client.read_gatt_char(charuuid))
        print(green("[+]RECV: ") + str(value))
    except:
        print(red("[x]ERROR: Can't read value from " + charuuid))

async def write_value(address,charuuid,value):
    try:
        await client.write_gatt_char(0x2b,bytes(value))
        print(green("[+]SEND: ") + bytes(value))
    except:
        print(red("[x]ERROR: Can't write value to " + charuuid))

###############################################################

async def main():
    f = Figlet(font="slant", width=100)
    print(f.renderText("BLE Security Tool"))
    print(" Author: yichen               Version: 0.01\n")
    meun = PrettyTable(["选项", "说明"])
    meun.align["选项"] = 'l'
    meun.align["说明"] = 'l'
    meun.add_row([yellow("help / h"),blue("展示帮助菜单")])
    meun.add_row([yellow("lescan"),blue("扫描周围低功耗蓝牙设备")])
    meun.add_row([yellow("connect"),blue("连接BLE设备")])
    meun.add_row([yellow("disconnect"),blue("断开BLE设备的连接")])
    meun.add_row([yellow("services"),blue("显示已连接设备的服务")])
    meun.add_row([yellow("characteristics"),blue("显示某一服务的属性")])
    meun.add_row([yellow("restart"),blue("重启蓝牙服务")])
    print(meun)
    choose = ""
    while choose != "exit":
        choose = input("--> ")
        if choose == "lescan":
            await scan_devices()
        if choose == "connect":
            address = input("MAC Address:")
            tmp = asyncio.create_task(connclient(address))
            client = await tmp
        if choose == "disconnect":
            tmp = asyncio.create_task(disconnclient(client))
            await tmp
        if choose == "services":
            tmp = asyncio.create_task(scan_services(client))
            await tmp
        if choose == "characteristics":
            serviceid = input("service uuid:")
            tmp = asyncio.create_task(scan_characteristics(client,serviceid))
            await tmp
        if choose == "clear":
            sys.stdout.write("\x1b[2J\x1b[H")
        if choose == "restart":
            os.system("service bluetooth restart")
        if choose == "h" or choose == "help":
            print(meun)

asyncio.run(main())