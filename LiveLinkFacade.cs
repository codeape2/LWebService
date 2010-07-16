using System;
using System.IO;

namespace LWebService {

public class LiveLinkFacade : ILiveLinkFacade {
    public string GetLoginToken(string username, string password) {
        throw new NotImplementedException();
    }

    public Stream GetFile(string token, string objectID, int version, bool rendition, string renditionType) {
        throw new NotImplementedException();
    }

    public string PutFile(System.IO.Stream content, string token, string contextID) {
        throw new NotImplementedException();
    }

    public string Search(string xmlsearchcriteria) {
        throw new NotImplementedException();
    }

    public string NewMetadata(string metadata) {
        throw new NotImplementedException();
    }
}

}
