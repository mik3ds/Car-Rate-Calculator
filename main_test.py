import unittest
import requests
import json

URL = 'http://localhost:5000/calculator'
payload = {
    'entryfield': '2019-12-06 06:30:00.000000',
    'exitfield': '2019-12-06 18:30:00.000000'
}

session = requests.session()
r = requests.post(URL, data=payload)

class EndToEndTests(unittest.TestCase):
    
    def test_sevice_is_running(self):
    	expected = json.loads('{"Price": "13", "Rate": "Early Bird"}')
    	self.assertEqual(json.loads(str(r.content, encoding='UTF-8')), expected)

if __name__ == '__main__':
    unittest.main()

