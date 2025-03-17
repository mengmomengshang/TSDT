from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):  # 注意方法名是 `setUp`，不是 `setup`
        self.browser = webdriver.Chrome()

    def tearDown(self):  # 方法名是 `tearDown`
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 用户故事：张三访问待办事项应用首页
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title, f"browser title was: {self.browser.title}")

        # 应用应包含一个文本输入框
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), '输入待办事项')

        # 张三输入第一个待办事项并提交
        inputbox.send_keys('Buy flowers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)  # 等待页面更新

        # 检查待办事项是否显示在列表中
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy flowers' for row in rows))

        # 继续输入第二个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Send a gift to Lisi')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # 检查两个待办事项均显示
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy flowers' for row in rows))
        self.assertTrue(any(row.text == '2: Send a gift to Lisi' for row in rows))

        # 验证生成的唯一 URL 是否有效
        self.fail('Finish the test!')  # 临时占位符，后续删除

if __name__ == '__main__':
    unittest.main()