import allure


class TestLogin:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('我是测试步骤001')
    def test_01(self):
        allure.attach('用户名', '输入用户名的描述')
        print('输入用户名')
        allure.attach('密码', '输入密码的描述')
        print('输入密码')
        allure.attach('登录', '点击登录按钮的描述')
        print('点击登录按钮')
        print(1)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('我是测试步骤002')
    def test_02(self):
        print(2)
        
    def test_03(self):
        print(3)
