"""
A module for communicating with Logica's LicenseWeb API.

"""
from __future__ import print_function
from urllib2 import urlopen
from urllib import urlencode

class LicenseWebClient(object):
    def __init__(self, url):
        self.url = url

    def authenticate(self, username, password):
        return urlopen("{0}/AuthenticateUser?username={1}&password={2}".format(
            self.url, username, password)).read()

    def download(self, token, objectid):
        return urlopen("{0}/DownloadFile?token={1}&objectid={2}".format(
            self.url, token, objectid)).read()

    def upload(self, token, contextID, filename):
        return urlopen("{0}/UploadFile?token={1}&contextID={2}".format(self.url, token, contextID), 
                open(filename, "rb").read()
                ).read()

    def downloadmetadata(self, search):
        return urlopen("{0}/DownloadMetadata".format(self.url), search).read()

if __name__ == "__main__":
    c = LicenseWebClient("http://localhost:8000")
    print("AuthenticateUser", c.authenticate("user", "pwd"))
    filecontents = c.download("foobar", 234)
    print("DownloadFile", filecontents[0:20] + "...", "({0} bytes)".format(len(filecontents)))
    #print("DownloadFile(invalid token)" , end="")
    #try:
    #    c.download("baz", 19)
    #except:
    #    import sys
    #    print(sys.exc_info()[1])

    print("UploadFile", c.upload(token="foobar", contextID="187xxy", filename="lwebclient.py"))
    #print("DownloadMetadata", c.downloadmetadata("<search><from>...</from><to>...</to></search>"))
    print("DownloadMetadata", c.downloadmetadata("boo"))


