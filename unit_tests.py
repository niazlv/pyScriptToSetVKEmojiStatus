# -*- coding: utf8 -*-

# # # # # # # # # # # # # # # # # # # # #
#   Module unit_tests.py writed         #
#       by Niyaz                        #
#   description:                        #
#       module for unittests            #
#   Created:    21.08.2022 02:12        #
#   Modify:     21.08.2022 04:14        #
# # # # # # # # # # # # # # # # # # # # #

import unittest

import functions
import vk_request
import read_write

class TestRead_write(unittest.TestCase):
    def test_readAppids(self):
        data1 = read_write.readAppids()
        self.assertGreaterEqual(len(data1),0)
    
    def test_appendAppid(self):
        self.assertTrue(read_write.appendAppid("123"))
        self.assertTrue(read_write.appendAppid("0"))
        self.assertTrue(read_write.appendAppid("345632"))
        self.assertTrue(read_write.appendAppid("5252523"))
    
    def test_removeAppid(self):
        self.assertTrue(read_write.removeAppid("123"))
        self.assertFalse(read_write.removeAppid("123"))
        self.assertTrue(read_write.removeAppid("0"))
        self.assertFalse(read_write.removeAppid("0"))
        self.assertTrue(read_write.removeAppid("345632"))
        self.assertFalse(read_write.removeAppid("345632"))
        self.assertTrue(read_write.removeAppid("5252523"))
        self.assertFalse(read_write.removeAppid("5252523"))

class TestFunction(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    
    def test_get_data_from_url(self):
        url1 = "https://oauth.vk.com/blank.html#access_token=vk1.a.ZZcr0ejrjZH8pxnW_mgiWz3pDA2T9cVSkWrOtEyuBA7HOeXmFvguHoNtT2NGB6Xb4lGwjh6Llz0yvRz1YE4BM2TwiQMKNy-nUhFro6UEKtpY-41gZOHOjkCgZhLq1sM1y0N0Hp7wraG1uEdrJxGJ9CVtZ4uWTQQN5dxf3g1-V2Trim-aCiyBLXDhzn-BoUpu&expires_in=86400&user_id=64077689"
        data1 = functions.get_data_from_url(url1)
        self.assertEqual(data1['access_token'], 'vk1.a.ZZcr0ejrjZH8pxnW_mgiWz3pDA2T9cVSkWrOtEyuBA7HOeXmFvguHoNtT2NGB6Xb4lGwjh6Llz0yvRz1YE4BM2TwiQMKNy-nUhFro6UEKtpY-41gZOHOjkCgZhLq1sM1y0N0Hp7wraG1uEdrJxGJ9CVtZ4uWTQQN5dxf3g1-V2Trim-aCiyBLXDhzn-BoUpu')
        self.assertEqual(data1['expires_in'], '86400')
        self.assertEqual(data1['user_id'], '64077689')

        data1 = functions.get_data_from_url('')
        self.assertEqual(data1['access_token'], '')
        self.assertEqual(data1['expires_in'], '')
        self.assertEqual(data1['user_id'], '')
        data1 = functions.get_data_from_url('vk1.a.ZZcr0ejrjZH8pxnW_mgiWz3pDA2T9cVSkWrOtEyuBA7HOeXmFvguHoNtT2NGB6Xb4lGwjh6Llz0yvRz1YE4BM2TwiQMKNy-nUhFro6UEKtpY-41gZOHOjkCgZhLq1sM1y0N0Hp7wraG1uEdrJxGJ9CVtZ4uWTQQN5dxf3g1-V2Trim-aCiyBLXDhzn-BoUpu')
        self.assertEqual(data1['access_token'], 'vk1.a.ZZcr0ejrjZH8pxnW_mgiWz3pDA2T9cVSkWrOtEyuBA7HOeXmFvguHoNtT2NGB6Xb4lGwjh6Llz0yvRz1YE4BM2TwiQMKNy-nUhFro6UEKtpY-41gZOHOjkCgZhLq1sM1y0N0Hp7wraG1uEdrJxGJ9CVtZ4uWTQQN5dxf3g1-V2Trim-aCiyBLXDhzn-BoUpu')
        self.assertEqual(data1['expires_in'], '')
        self.assertEqual(data1['user_id'], '')
        data1 = functions.get_data_from_url('4fwhiugfhw4ughiuawhfiuahg4iushe4i')
        self.assertEqual(data1['access_token'], '')
        self.assertEqual(data1['expires_in'], '')
        self.assertEqual(data1['user_id'], '')

    def test_is_token_valid(self):
        self.assertTrue(functions.is_token_valid('vk1.a.ZZcr0ejrjZH8pxnW_mgiWz3pDA2T9cVSkWrOtEyuBA7HOeXmFvguHoNtT2NGB6Xb4lGwjh6Llz0yvRz1YE4BM2TwiQMKNy-nUhFro6UEKtpY-41gZOHOjkCgZhLq1sM1y0N0Hp7wraG1uEdrJxGJ9CVtZ4uWTQQN5dxf3g1-V2Trim-aCiyBLXDhzn-BoUpu'))
        self.assertFalse(functions.is_token_valid('vk1.a.ZZcr0ejrjZH8pxnW_mgiWz3pDA2T9cVSkWrOtEyuBA7HOeXmFvguHoNtT2NGB6Xb4lGwjh6Llz0yvRz1YE4BM2TwiQMKNy-nUhFro6UEKtpY-41gZOHOjkCgZhLq1sM1y0N0Hp7wraG1uEdrJxGJ9CVtZ4uWTQQN5dxf3g1-V2Trim-aCiyBLXDhzn-BoUp'))
        self.assertFalse(functions.is_token_valid('ehegeavucwithniuav'))
    
    # REMOVE all disabled appids from list
    def test_is_appid_valid(self):
        appids = read_write.readAppids()
        for i in range(0,len(appids)):
            if(not functions.is_appid_valid(appids[i])):
                print(appids[i]+" is invalid appid! Remove him from list...")
                if(not read_write.removeAppid(appids[i])):
                    print(appids[i]+" ERROR remove this appid from list!!!!!!!! check manualy")
            #self.assertTrue(functions.is_appid_valid(appids[i]))

class TestVk_request(unittest.TestCase):
    def test_vk_api_request(self):
        data1 = vk_request.vk_api_request(functions.methods['getImageList'],read_write.readAppids()[0],"test")
        self.assertEqual(data1['error']['error_code'],5)
        for i in range(0,len(data1['error']['request_params'])):
            if(data1['error']['request_params'][i]['key'] == 'api_id'):
                self.assertEqual(data1['error']['request_params'][i]['value'],read_write.readAppids()[0])
            if(data1['error']['request_params'][i]['key'] == 'method'):
                self.assertEqual(data1['error']['request_params'][i]['value'],functions.methods['getImageList'])
            


if __name__ == '__main__':
    unittest.main()