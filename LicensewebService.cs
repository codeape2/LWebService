using System;
using System.IO;

namespace LWebService {

public class LicensewebService : ILicensewebService {
    // For integrasjonstesting, uten LiveLink
    ILiveLinkFacade livelink = new MockLiveLinkFacade();
    
    // Produksjon:
    //ILiveLinkFacade livelink = new LiveLinkFacade();
    
    public string AuthenticateUser(string username, string password) {
 	    return livelink.GetLoginToken(username, password);
    }
    
    public Stream DownloadFile(string token, string objectID, int version, bool rendition, string renditionType) {
        return livelink.GetFile(token, objectID, version, rendition, renditionType);
    }
    
    public string UploadFile(Stream content, string token, string contextID) {
        return livelink.PutFile(content, token, contextID);
    }
    
    public Stream DownloadMetadata(Stream search) {
        var reader = new StreamReader(search);
        var retval = new MemoryStream();
        var writer = new StreamWriter(retval);
        
        writer.Write(livelink.Search(reader.ReadToEnd()));
        
        writer.Flush();
        retval.Position = 0;
        return retval;
    }
    
    public string UploadMetadata(Stream metadata) {
        return livelink.NewMetadata(new StreamReader(metadata).ReadToEnd());
    }
    

}

}