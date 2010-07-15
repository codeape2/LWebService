﻿using System;
using System.IO;

namespace LWebService {

public class LicensewebService : ILicensewebService {
    ILiveLinkFacade livelink = new MockLiveLinkFacade();
    
    public string AuthenticateUser(string username, string password) {
 	    return livelink.GetLoginToken(username, password);
    }
    
    public Stream DownloadFile(string token, string objectID, int version, bool rendition, string renditionType) {
        return livelink.GetFile(token, objectID, version, rendition, renditionType);
    }
    
    public string UploadFile(Stream content, string token, string contextID) {
        return livelink.PutFile(content, token, contextID);
    }
    
    public string DownloadMetadata(string xmlsearchcriteria) {
        return livelink.Search(xmlsearchcriteria);
    }
    

}

}