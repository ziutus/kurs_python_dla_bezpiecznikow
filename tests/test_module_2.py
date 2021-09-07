import unittest
import re

def is_admin_user_file(filepath):
    # if re.search('\/[^/]*admin[^/]*.php$|\/[^/]*user[^/]*.php$', filepath) and not re.search('.*admin.*\/|.*user.*\/', filepath):
    if re.search('\/[^/]*admin[^/]*.php$|\/[^/]*user[^/]*.php$', filepath):
        return True
    return False


class MyTestCase(unittest.TestCase):
    def test_path_regex(self):
        self.assertEqual(is_admin_user_file("wp-admin/css/customize-controls.min.css"), False)
        self.assertEqual(is_admin_user_file("wp-admin/admin-functions.php"), True)
        self.assertEqual(is_admin_user_file("wp-activate.php"), False)
        self.assertEqual(is_admin_user_file("wp-admin/functions.php"), False)
        self.assertEqual(is_admin_user_file("wp-admin/css/wp-admin.css"), False)
        self.assertEqual(is_admin_user_file("wp-admin/custom-background.php"), False)
        self.assertEqual(is_admin_user_file("wp-admin/ms-admin.php"), True)
        self.assertEqual(is_admin_user_file("wp-misiek/ms-admin.php"), True)


if __name__ == '__main__':
    unittest.main()
