from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from loginInfo import email, password
import time

#open chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

#sign in with FB
driver.get('https://www.facebook.com/login.php?skip_api_login=1&api_key=428250913904849&kid_directed_site=0&app_id=428250913904849&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.12%2Fdialog%2Foauth%3Fauth_type%3Drerequest%26response_type%3Dcode%26display%3Dpopup%26client_id%3D428250913904849%26scope%3Demail%252Cuser_birthday%252Cuser_location%252Cuser_photos%252Cuser_friends%252Cuser_gender%252Cuser_likes%26state%3DMjVmY2U1YjA4YmQwZTI4NTI1YmU5ZGE4YWRjM2QyMjIwODVkZmUzYWNjZTQxNTIyODMzMDIzNzllYjBkMjZjNnxodHRwczovL3VzMS5idW1ibGUuY29tL2ZhY2Vib29rL2F1dGhvcml6ZS5waHRtbD9ydD0wMzk4NjUmbW9iaWxlX3JldHVybj1odHRwcyUzQSUyRiUyRmJ1bWJsZS5jb20lMkZzdGF0aWMlMkZleHRlcm5hbC1hdXRoLXJlc3VsdC5odG1sJTNG%26redirect_uri%3Dhttps%253A%252F%252Fbumble.com%252Fexternal%252Fredirector.phtml%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D17406632-4f91-49b8-b1c3-c055d9f61bb7&cancel_url=https%3A%2F%2Fbumble.com%2Fexternal%2Fredirector.phtml%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DMjVmY2U1YjA4YmQwZTI4NTI1YmU5ZGE4YWRjM2QyMjIwODVkZmUzYWNjZTQxNTIyODMzMDIzNzllYjBkMjZjNnxodHRwczovL3VzMS5idW1ibGUuY29tL2ZhY2Vib29rL2F1dGhvcml6ZS5waHRtbD9ydD0wMzk4NjUmbW9iaWxlX3JldHVybj1odHRwcyUzQSUyRiUyRmJ1bWJsZS5jb20lMkZzdGF0aWMlMkZleHRlcm5hbC1hdXRoLXJlc3VsdC5odG1sJTNG%23_%3D_&display=popup&locale=en_US')
time.sleep(3)

#Fill in Email and password
e = driver.find_element_by_xpath('//*[@id="email"]')
e.send_keys(email)
p = driver.find_element_by_xpath('//*[@id="pass"]')
p.send_keys(password)
login = driver.find_element_by_xpath('//*[@id="u_0_0"]')
login.click()
time.sleep(2)

#login to bumble
signInBumble = driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
signInBumble.click()
time.sleep(2)
fbBtn = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div')
fbBtn.click()
time.sleep(12)


swipeRightKey = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/span/span')

#swiping
i = 0
while i < 550:
    swipeRightKey.click()
    time.sleep(.2)
    print(i)
    i += 1

print('Done swiping.... Good Luck!')
#exit program
driver.close()
