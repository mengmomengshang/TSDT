from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):
    def setUp(self):  # 注意方法名是 `setUp`，不是 `setup`
        self.browser = webdriver.Chrome()

    def tearDown(self):  # 方法名是 `tearDown`
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 张三听说有一个在线待办事项的应用
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 他注意到网页的标题和头部都包含"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text #(1)
        self.assertIn('To-Do', header_text)

        # 应用有一个输入待办事项的文本输入框
        inputbox = self.browser.find_element(By.ID,'id_new_item') #(1)
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 他在文本输入框中输入了"Buy flowers"
        inputbox.send_keys('Buy flowers') #(2)

        # 他按了回车键后，页面更新了
        # 待办事项表格中显示了"1:Buy flowers"
        inputbox.send_keys(Keys.ENTER) #(3)
        time.sleep(1)  #(4)

        table = self.browser.find_element(By.ID,'id_list_table')
        rows = table.find_elements(By.TAG_NAME,'tr') #(1)
        self.assertIn('1: Buy flowers', [row.text for row in rows])

        # 页面中又显示了一个文本输入框，可以输入其他待办事项
        # 他输入了"gift to girlfriend"
        #inputbox = self.browser.find_element_by_id('id_new_item')
        #inputbox.send_keys('Send a gift to Lisi')
        #inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)

        # 检查两个待办事项均显示
        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        #self.assertTrue(any(row.text == '1: Buy flowers' for row in rows))
        #self.assertTrue(any(row.text == '2: Send a gift to Lisi' for row in rows))

        # 验证生成的唯一 URL 是否有效
        self.fail('Finish the test!')  

if __name__ == '__main__':
    unittest.main()