import store_parser
import unittest

class GoogleplayTestSuit(unittest.TestCase):

    def test_googleplay(self):
        url = 'https://play.google.com/store/apps/details?id=com.android.chrome'

        parsed = store_parser.parse_googleplay(url)

        self.assertIsNotNone(parsed)
        self.assertIn('name', parsed)
        self.assertIn('author', parsed)
        self.assertIn('description', parsed)
        self.assertIn('icon_url', parsed)

        self.assertEqual('Google Inc.', parsed['author'])

    def test_appstore(self):
        url = 'https://itunes.apple.com/us/app/sonic-dash/id582654048'

        parsed = store_parser.parse_appstore(url)

        self.assertIsNotNone(parsed)
        self.assertIn('name', parsed)
        self.assertIn('author', parsed)
        self.assertIn('description', parsed)
        self.assertIn('icon_url', parsed)

        self.assertEqual('By SEGA', parsed['author'])

if __name__ == '__main__':
    unittest.main()
