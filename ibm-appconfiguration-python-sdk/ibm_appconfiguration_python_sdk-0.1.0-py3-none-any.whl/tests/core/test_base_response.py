# Copyright 2021 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest
from ibm_appconfiguration.core.base_request import BaseResponse
from requests.models import Response


class MyTestCase(unittest.TestCase):

    def test_response(self):
        response = Response()
        response.status_code = 200
        response._content = b'{ "message" : "Not Found" }'
        headers = {
            "status": 200
        }
        status_code = 200

        base_response = BaseResponse(response, headers, status_code)

        self.assertEqual(base_response.get_status_code(), status_code)
        self.assertEqual(base_response.get_headers(), headers)
        self.assertEqual(base_response.get_result(), response)

        result = {
            'result': 'HTTP response',
            'headers': headers,
            'status_code': status_code
        }

        self.assertEqual(base_response._to_dict(), result)
        self.assertIsNotNone(base_response.__str__())



if __name__ == '__main__':
    unittest.main()
