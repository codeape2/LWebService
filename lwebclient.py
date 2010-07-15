"""
A module for communicating with Logica's LicenseWeb API.

"""
from __future__ import print_function
from urllib2 import urlopen

class LicenseWebClient(object):
    def __init__(self, url):
        self.url = url

    def authenticate(self, username, password):
        return urlopen("{0}/AuthenticateUser?username={1}&password={2}".format(
            self.url, username, password)).read()

    def download(self, token, objectid):
        return urlopen("{0}/DownloadFile?token={1}&objectid={2}".format(
            self.url, token, objectid)).read()

    def upload(self, filename):
        return urlopen("{0}/UploadFile".format(self.url), 
                {"content": open(filename, "rb")}).read()

if __name__ == "__main__":
    c = LicenseWebClient("http://localhost:8000")
    print("AuthenticateUser", c.authenticate("user", "pwd"))
    filecontents = c.download("foobar", 234)
    print("DownloadFile", filecontents[0:20] + "...", "({0} bytes)".format(len(filecontents)))
    print("UploadFile", c.upload("lwebclient.py"))


