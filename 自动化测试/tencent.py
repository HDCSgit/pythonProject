# -*-coding:utf-8-*-
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By
from selenium.webdriver.common import by
import time

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "BLA-AL00",
    "appPackage": "com.tencent.mobileqq",
    "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
    "noReset": "true"
}