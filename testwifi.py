import pywifi
from pywifi import const    # 引用一些常量


# 判断是否已经连接到wifi
def gic():
    # 创建一个对象
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 打印网卡名称
    # print(ifaces.name())
    # get a list
    # print(ifaces)
    # 打印网卡连接状态
    print(ifaces.status())
    print(const.IFACE_CONNECTED)
    if ifaces.status() == const.IFACE_CONNECTED:
        print("已连接")
    else:
        print("未连接")


gic()


# 扫描附近的wifi
def bies():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    # 扫描wifi
    ifaces.scan()
    # 获取扫描结果
    result = ifaces.scan_results()
    for data in result:
        # ssid 是wifi名称
        print(data.ssid)


bies()

