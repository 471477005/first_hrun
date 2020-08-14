import os

os.chdir(r'D:\启明星\first_httprunner\testcases')
print(os.getcwd())
os.system('hrun ../testcases')
os.system('pytest --alluredir ../report/allure_raw --clean-alluredir')
os.system('allure serve ../report/allure_raw')
