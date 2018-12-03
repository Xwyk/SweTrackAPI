import requests
import time


class Session():
    def __init__(self, username="", password="", url=""):
        self.username = username
        self.password = password
        self.baseUrl = url
        self.session = None

    def __del__(self):
        self.logout()

    def login(self):
        if self.session == None:
            response = requests.post( self.baseUrl + '/login', data = {'Username':self.username, 'Password':self.password})
            self.session = response.json()
            
            #print("Session Loggin:" + repr(self.session))
            
            if "error" in self.session:
                print( "Unable to login: ", data["error"] )
                return False
            if not "AccessToken" in self.session:
                print( "Unable to login: AccessToken missing.")
                return False
            
        return True

    def logout(self):
        self.session = None
        return True

    def get(self, url, payload=None):
        self.login()
        try:
            url = self.baseUrl + url
            headers = {'Authorization': self.session["AccessToken"]}
            r = requests.get(url, params=payload, headers=headers)
            #print( "HttpGetUrl:", r.url )
            #print( "HttpGetData: ", r.text)
            #print( "HttpGetHeaders: ", r.headers)
            #print( "HttpGetRequestHeaders: ", r.request.headers)
        except Exception as exc:
            self.session = None
            raise
        return r.json()

    def post(self, url, payload):
        self.login()
        try:
            url = self.baseUrl + url
            headers = {'Authorization': self.session["AccessToken"]}
            r = requests.post( url, json=payload, headers=headers )
            #print( "HttpPostUrl:", url )
            #print( "HttpPostPayload:", payload )
            #print( "HttpPostData:", r.text )
        except Exception as exc:
            self.session = None
            raise
        return r.json()

    def put(self, url, payload):
        self.login()
        try:
            url = self.baseUrl + url
            headers = {'Authorization': self.session["AccessToken"]}
            r = requests.put( url, json=payload, headers=headers )
            #print( "HttpPutUrl:", url )
            #print( "HttpPutPayload:", payload )
            #print( "HttpPutData:", r.text )
        except Exception as exc:
            self.session = None
            raise
        return r.json

        
        
class Api():
    def __init__(self, username, password, url="https://www.gpscloud.se/api"):
        session = Session(username, password, url)
        self.session = session

    def getDevices(self):
        """ Get all devices """
        url = "/getDevices"
        data = self.session.get(url)
        #print( "RAW-getDevices:", data )
        return data

    def getAlerts(self):
        """ Get Alerts """
        url = "/larm"
        data = self.session.get(url)
        #print( "RAW-getAlerts:", data )
        return data

    def getAccountSettings(self):
        """ Get Account Settings """
        url = "/getAccountSettings"
        data = self.session.get(url)
        #print( "RAW-getAccountSettings:", data )
        return data

    def getReceipts(self):
        """ Get Receipts """
        url = "/kvitto"
        data = self.session.get(url)
        #print( "RAW-getReceipts:", data )
        return data        
        
    def getIccIdInfo(self):
        """ Get ICC Id Info """
        url = "/geticcidinfo"
        data = self.session.get(url)
        #print( "RAW-getIccIdInfo:", data )
        return data        
        
    def getPositionHistory(self, DeviceId=0, FromDate=time.time(), ToDate=time.time()):
        """ Get Position History """
        url = "/getPositionHistory"
        payload = {"DeviceID": str(DeviceId), "FROM": self.ConvertToDate(FromDate), "TO": self.ConvertToDate(ToDate)}
        data = self.session.post(url, payload)
        print( "RAW-getPositionHistory:", data, payload )
        return data        
        
    def ConvertToDate(self, Date=time.time()):
        return time.strftime("%Y-%m-%d %H:%M:00", time.gmtime(Date))
        
        
