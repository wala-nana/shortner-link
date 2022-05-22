import unittest
from ..controllers import shortner_controller as controller
from sqlalchemy.orm import Session


class TestingShortner(unittest.TestCase):

    def test_encode_link(self):

        link={"link_name": "test","link_url": "https://frappe.school/courses/frappe-framework-tutorial/learn/6.3"}
        method_testing = controller.encode_link(link, db = Session )
        expected_result = {"The Shortened URL is: ": "https://tinyurl.com/y39e6jjo"}

        self.assertEqual(method_testing, expected_result)


    def test_get_long_link(self):
        self.assertEqual(controller.get_long_link(short_link={"link_url": "https://tinyurl.com/y39e6jjo"}, db = Session ), {"The original url is: ": "https://frappe.school/courses/frappe-framework-tutorial/learn/6.3"})


if __name__ == '__main__':
    unittest.main()