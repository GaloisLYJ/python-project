import time
import uiautomator2

# 面试官您好 我是刘宇健 现在测试的是一个对安卓apk模拟点击的自动化测试脚本
# 主要的运行效果是 切换登陆状态，滑动测试，界面切换和功能点击等

# 驱动器 控制器
d = uiautomator2.connect_usb('127.0.0.1:62026')

# 启动apk
d.xpath('//*[@resource-id="com.vphone.launcher:id/workspace"]/android.view.View[1]/android.view.View[1]/android.widget.TextView[9]').click();
time.sleep(5)

# 退出登陆
sl = d.xpath('//*[@text=" 我的"]')
# 等待3s, 没有找到会返回None (等待元素加载完毕)
sl.wait(timeout=3)
if sl.exists:
    # if d.xpath('//*[@text=" 我的"]').exists:
    print("已经登陆，先退出")
    d.xpath('//*[@text=" 我的"]').click()
    time.sleep(2)
    d.xpath('//*[@text=" 设置"]').click()
    time.sleep(2)
    d.xpath('//*[@text="退出登錄 "]').click()

sl2 = d.xpath('//*[@resource-id="login-btn"]')
sl2.wait(timeout=3)
if sl2.exists:
    print('尚未登陆，输入参数')
    time.sleep(2)
    # 输入账号
    d.xpath('//*[@text="会员登录"]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[2]').set_text('17722799521')
    time.sleep(2)

    # 输入密码
    d.click(0.384, 0.368)
    d.send_keys("791089", clear=True)
    time.sleep(2)

    # 点击登陆
    d.xpath('//*[@resource-id="login-btn"]').click()
    time.sleep(2)

    # 主界面切换测试
    d.xpath('//*[@text=" 我的"]').click();
    time.sleep(2)
    d.xpath('//*[@text=" 猴集市"]').click();
    time.sleep(2)

    # 滑动测试
    d(scrollable=True).scroll.toEnd();
    time.sleep(2)
    d(scrollable=True).scroll.toBeginning();
    time.sleep(2)
    d(scrollable=True).scroll.toEnd();

sl3 = d.xpath('//*[@text="嘉福猴"]/android.view.View[2]/android.view.View[1]/android.view.View[7]/android.view.View[1]/android.widget.Button[1]')
sl3.wait(timeout=3)
if sl3.exists:
    print("还未预约，点击预约")
    sl3.click()

# 抢购测试（到达指定时间触发点击）
d(scrollable=True).scroll.to(text="領養")
d.xpath('//*[@text="領養"]').click()
print("finish click")