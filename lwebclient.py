"""
A module for communicating with Logica's LicenseWeb API.

Example:

    from lwebclient import LicenseWebClient
    c = LicenseWebClient("http://url/to/service/")
    token = c.authenticate("username", "password")
    ...

"""
from __future__ import print_function
from urllib2 import urlopen
from urllib import urlencode
from xml.etree import ElementTree as E
import codecs

class LicenseWebClient(object):
    def __init__(self, url):
        self.url = url

    def authenticate(self, username, password):
        return E.fromstring(urlopen("{0}/AuthenticateUser?username={1}&password={2}".format(
            self.url, username, password)).read()).text

    def download(self, token, objectid):
        return urlopen("{0}/DownloadFile?token={1}&objectid={2}".format(
            self.url, token, objectid)).read()

    def upload(self, token, contextID, filename):
        return urlopen("{0}/UploadFile?token={1}&contextID={2}".format(self.url, token, contextID), 
                open(filename, "rb").read()
                ).read()

    def downloadmetadata(self, search):
        return E.fromstring(urlopen("{0}/DownloadMetadata".format(self.url), search).read()).text

    def uploadmetadata(self, metadata):
        return urlopen("{0}/UploadMetadata".format(self.url), metadata).read()

URL = "http://localhost/L2SService/L2S_service.svc"
#URL = "http://localhost:2636/L2S_service.svc"
USER = "admin"
PWD = "livelink"

if __name__ == "__main__":
    c = LicenseWebClient(URL)
    token = c.authenticate(USER, PWD)
    print("AuthenticateUser:", token)

    search_xml = codecs.open("dlmetadata2.xml").read().format(token=token)
    print(search_xml)
    search_result = c.downloadmetadata(search_xml)
    print(type(search_result)) # str
    print(search_result, file=open("search_result.xml", "w"))

    """
    filecontents = c.download(token="foobar", objectid=234)
    print("DownloadFile:", filecontents[0:20] + "...", "({0} bytes)".format(len(filecontents)))
    #print("DownloadFile(invalid token)" , end="")
    #try:
    #    c.download("baz", 19)
    #except:
    #    import sys
    #    print(sys.exc_info()[1])

    print("UploadFile:", c.upload(token="foobar", contextID="187xxy", filename="lwebclient.py"))
    print("DownloadMetadata:", c.downloadmetadata("<search><from>...</from><to>...</to></search>"))
    print("UploadMetadata:", c.uploadmetadata("<metadata><doctitle>foo</doctitle></metadata>"))
    """


