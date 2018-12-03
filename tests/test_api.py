from unittest import TestCase

from pyswetrack import *

from .config import *

class ApiTest(TestCase):

    def test_getDevices(self):
        myApi = Api(swetrack_username, swetrack_password)
        data = myApi.getDevices()
        print("getDevices:" + repr(data))
        self.assertTrue(data != None)

    def test_getAlerts(self):
        myApi = Api(swetrack_username, swetrack_password)        
        data = myApi.getAlerts()
        print("getAlerts:" + repr(data))
        self.assertTrue(data != None)
        
    def test_getAccountSettings(self):
        myApi = Api(swetrack_username, swetrack_password)
        data = myApi.getAccountSettings()
        print("getAccountSettings:" + repr(data))
        self.assertTrue(data != None)
        
    def test_getReceipts(self):
        myApi = Api(swetrack_username, swetrack_password)
        data = myApi.getReceipts()
        print("getReceipts:" + repr(data))
        self.assertTrue(data != None)
        
    def test_getIccIdInfo(self):
        myApi = Api(swetrack_username, swetrack_password)
        data = myApi.getIccIdInfo()
        print("getIccIdInfo:" + repr(data))
        self.assertTrue(data != None)
        
    def test_getPositionHistory(self):
        data = None
        timeNow = time.time()
        timeBefore = timeNow - 3600.0 # 1 hour
        myApi = Api(swetrack_username, swetrack_password)
        myDevices = myApi.getDevices()
        for device in myDevices[1]:
            if "id" in device:
                data = myApi.getPositionHistory(device["id"],timeBefore,timeNow)
                print("getPositionHistory:" + repr(data))
        self.assertTrue(data != None)
        
    

        
