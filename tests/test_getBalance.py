import responses
import requests
import urllib.parse
import unittest
from vkmix import VkMix

class TestVkMix(unittest.TestCase):
    def response_callback(self, resp):
        resp.callback_processed = True
        args = {}
        try:
            args = urllib.parse.parse_qs(urllib.parse.urlparse(resp.url)[4])
        except AttributeError: pass
        except KeyError: pass
        self.assertIn("api_token", args)
        return resp

    def test_getBalance(self):
        with responses.RequestsMock(response_callback=self.response_callback) as m:
            m.add(responses.GET, "https://vkmix.com/api/2/getBalance", json={"response":24.64})
            vkm = VkMix(api_token="mykey")
            data = vkm.getBalance()
            self.assertEqual(data, 24.64)

if __name__ == "__main__":
    unittest.main()
    