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
import re

class LicenseWebClient(object):
    def __init__(self, url):
        self.url = url

    def authenticate(self, username, password):
        return E.fromstring(urlopen("{0}/AuthenticateUser?username={1}&password={2}".format(
            self.url, username, password)).read()).text

    def downloadfile(self, token, object_id, version, rendition, renditionType):
        return urlopen("{0}/DownloadFile?token={1}&ID={2}&ver={3}&rendition={4}&type={5}".format(
            self.url, token, object_id, version, rendition, renditionType)).read()

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
SEARCHFILE = "dlmetadata3.xml"

if __name__ == "__main__":
    c = LicenseWebClient(URL)
    token = c.authenticate(USER, PWD)
    print("AuthenticateUser:", token)

    search_xml = codecs.open(SEARCHFILE).read().format(token=token)
    print(search_xml)
    search_result = c.downloadmetadata(search_xml)
    print(search_result, file=open("search_result.xml", "w"))

    result = E.fromstring(search_result[39:])
    print("Documents:")
    for document in result.findall("documents/document"):
        object_id = document.find("object_id").text
        version = document.find("version").text
        file_content = c.downloadfile(token, object_id, version, "false", "")
        print("Length:", len(file_content))
        print("Content:", file_content)

