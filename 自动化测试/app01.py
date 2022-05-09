from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By

# 如果需要清空缓存,删除“noReset”: "true"
desired_caps = {
    "platformName": "Android",
    "platformVersion": "10.0",
    "deviceName": "6QDDU19702033073",
    "appPackage": "com.haixiaep",
    "appActivity": "com.sinosun.tchats.WiWelcomeActivity",
    "noReset": "true"


}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

print('ok')

# 设置缺省等待时间
driver.implicitly_wait(10)

"""

# 隐私政策确定
privacy = driver.find_element(By.ID,'com.haixiaep:id/html_agree')
if privacy:
    privacy.click()

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
"""

mylogging = driver.find_element(By.ID,'com.haixiaep:id/fifthicon')
menu = driver.find_element(By.ID,'com.haixiaep:id/menu_fifth')
otherLoggings = driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.TextView')
passwordLoging = driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.TextView[1]')
phoneNumber = driver.find_element(By.ID,'phone1')
phonePassword = driver.find_element(By.ID,'passwordView')
loggingAgreement = driver.find_elements(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]')
loggingCommit = driver.find_elements(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.widget.TextView')


try:
    if mylogging:
        mylogging.click()
    if otherLoggings:
        otherLoggings.click()
    if passwordLoging:
        passwordLoging.click()
    if phoneNumber:
        phoneNumber.send_keys('13695112111')
    if phonePassword:
        phonePassword.send_keys('Zxcvbn12')
    if loggingAgreement:
        loggingAgreement.click()
    if loggingCommit:
        loggingCommit.click()
except:
    pass

