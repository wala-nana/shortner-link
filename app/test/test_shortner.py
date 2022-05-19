import unittest
from ..controllers import shortner_controller as sh_c

from sqlalchemy.orm import Session


class TestingShortner(unittest.TestCase):
    def test_encode_link(self):

        # a = {"link_name": "test","link_url": "https://frappe.school/courses/frappe-framework-tutorial/learn/6.3"}
        # b = {"The Shortened URL is: ": "https://tinyurl.com/y39e6jjo"}
        # x = sh_c.encode_link(a,b)
        # print(x , "xxxxxxxxxxxxxxx")
        self.assertEqual(sh_c.encode_link({"link_name": "test","link_name": "test","link_url": "https://frappe.school/courses/frappe-framework-tutorial/learn/6.3"}, db = Session ), {"The Shortened URL is: ": "https://tinyurl.com/y39e6jjo"})


    def test_get_long_link(self):

        # a = {
        #         "link_url": "https://tinyurl.com/y39e6jjo"
        #     }
        # b = {"The original url is: ": "https://frappe.school/courses/frappe-framework-tutorial/learn/6.3"}
        # x = sh_c.encode_link(a,b)
        # print(x , "xxxxxxxxxxxxxxx")
        self.assertEqual(sh_c.get_long_link({"link_url": "https://tinyurl.com/y39e6jjo"}, db = Session ), {"The original url is: ": "https://frappe.school/courses/frappe-framework-tutorial/learn/6.3"})



if __name__ == '__main__':
    unittest.main()