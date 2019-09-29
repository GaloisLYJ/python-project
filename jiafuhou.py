import time
import uiautomator2

# 驱动器 控制器
d = uiautomator2.connect_usb('127.0.0.1:62001')
d2 = uiautomator2.connect_usb('127.0.0.1:62025')
d3 = uiautomator2.connect_usb('127.0.0.1:62026')
d4 = uiautomator2.connect_usb('127.0.0.1:62027')
d5 = uiautomator2.connect_usb('127.0.0.1:62028')
# d6 = uiautomator2.connect_usb('127.0.0.1:62029')

# 当前时间
now_time = time.localtime()
# 目标时间(电脑时间比北京时间快了5/6秒) 电脑休眠模拟器时间不会走 所以要提前设置
target_time = time.strptime("2019-09-28 19:30:12", "%Y-%m-%d %H:%M:%S")

# 距离目标的点击时间
diff = (target_time.tm_hour - now_time.tm_hour) * 60 * 60 + (
            target_time.tm_min - now_time.tm_min) * 60 + (
                         target_time.tm_sec - now_time.tm_sec)
print(diff)

time.sleep(diff)
print(time.localtime())
count = 1;
while count < 3:
 d.xpath('//*[@text="領養"]').click()
 d5.xpath('//*[@text="領養"]').click()
 d4.xpath('//*[@text="領養"]').click()
 d2.xpath('//*[@text="領養"]').click()
 d3.xpath('//*[@text="領養"]').click()

# d5.xpath('//*[@text="領養"]').click()
# d6.xpath('//*[@text="領養"]').click()
 count = count + 1
print("finish click 19:30")


