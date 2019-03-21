from Pages import RegisterPage

rp=RegisterPage.RegisterPage('firefox')
rp.emailfield.send_keys('is it working ??')
rp.emailfield.clear()
rp.usernamefield.send_keys('goodddaaaamnnn')
rp.passwordfield.send_keys('asd')
rp.registerbutton.click()