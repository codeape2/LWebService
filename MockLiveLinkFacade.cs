using System.Diagnostics;
using System.IO;

namespace LWebService {

public class MockLiveLinkFacade : ILiveLinkFacade {
    public string GetLoginToken(string username, string password) {
        return "foobar";
    }
    
    public Stream GetFile(string token, string objectID, int version, bool rendition, string renditionType) {
        var retval = new MemoryStream();
        var streamWriter = new StreamWriter(retval);
        while (retval.Length < 10*1024) {
            streamWriter.Write(string.Format("{0}{1}{2}{3}{4}", token, objectID, version, rendition, renditionType));
        }
        retval.Position = 0;
        return retval;
    }
}
}