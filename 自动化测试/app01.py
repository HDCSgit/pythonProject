# -*-coding:utf-8-*-

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By
from selenium.webdriver.common import by
import time

# 如果需要清空缓存,删除“noReset”: "true"
desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "BLA-AL00",
    "appPackage": "com.haixiaep",
    "appActivity": "com.sinosun.tchats.WiWelcomeActivity",
    "noReset": "true"


}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


# 设置缺省等待时间
driver.implicitly_wait(15)



# 隐私政策确定
privacy = driver.find_element(By.ID,'com.haixiaep:id/html_agree')
if privacy:
    privacy.click()
time.sleep(3)
# 是否允许访问媒体文件
accessMedia = driver.find_element(By.ID,'com.android.permissioncontroller:id/permission_allow_button')
if accessMedia:
    accessMedia.click()

# 是否允许“海企来”获取设备信息
deviceInformation = driver.find_element(By.ID,'com.android.permissioncontroller:id/permission_allow_button')
if deviceInformation:
    deviceInformation.click()


# 重要信息自启动，点击取消,且不再提示
neverKnow = driver.find_element(By.ID,'com.haixiaep:id/selectedImg')
if neverKnow:
    neverKnow.click()
iknow = driver.find_element(By.ID,'com.haixiaep:id/negative_bt')
if iknow:
    iknow.click()


mylogging = driver.find_element(By.ID,"com.haixiaep:id/fifthicon")
otherLoggings = driver.find_element(By.XPATH,"//android.view.View[@text='其他方式登录']")
passwordLogging = driver.find_element(By.XPATH,"//android.view.View[@text='密码登录']")
phoneNumberDelete = driver.find_element(By.XPATH,"//android.view.View[1][@index='1']")
phoneNumber = driver.find_element(By.XPATH,"//android.widget.EditText[@index='0']")
phonePassword = driver.find_element(By.XPATH,"//android.view.View[@resource-id='passwordView']")
loggingAgreement = driver.find_element(By.XPATH,"//android.view.View[@index='7']")
loggingCommit = driver.find_element(By.XPATH,"//android.widget.TextView[@text='登录']")


print('ok')
#操作
if mylogging:
    mylogging.click()

otherLoggings.click()
passwordLogging.click()
phoneNumberDelete.click()
phoneNumber.send_keys('13695112111')
password = 'Zxcvbn12'
for i in password:
    if phonePassword.get(i):
        phonePassword.press_keycode(phonePassword[i])
    else:
        phonePassword.press_keycode(phonePassword[i.lower()],64,59)

loggingAgreement.click()
loggingCommit.click()



