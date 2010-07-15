using System;
using System.Diagnostics;
using System.IO;

namespace LWebService {


public class MockLiveLinkFacade : ILiveLinkFacade {
    public string GetLoginToken(string username, string password) {
        Console.WriteLine(string.Format("Logging in user {0}", username));
        return "foobar";
    }
    
    public Stream GetFile(string token, string objectID, int version, bool rendition, string renditionType) {
        if (token != "foobar") throw new ArgumentException("Invalid token");
        
        var retval = new MemoryStream();
        var streamWriter = new StreamWriter(retval);
        while (retval.Length < 10*1024) {
            streamWriter.Write(string.Format("{0}{1}{2}{3}{4}", token, objectID, version, rendition, renditionType));
        }
        retval.Position = 0;
        
        Console.WriteLine("Sending file to client");
        
        return retval;
    }
    
    public string PutFile(Stream content, string token, string contextID) {
        if (token != "foobar") throw new ArgumentException("Invalid token");
        
        var outputfile = new FileStream("uploaded.file", FileMode.Create, FileAccess.Write);
        copyStream(content, outputfile);
        outputfile.Close();
        
        Console.WriteLine("File saved");
        
        return "file_saved";
    }
    
    public string Search(string searchcriteria) {
        Console.WriteLine("Searching: " + searchcriteria);
        return "<response><documents>...</documents></response>";
    }

    private void copyStream(Stream input, Stream output) {
        var buffer = new byte[32768];
        var read = 0;
        while ((read = input.Read(buffer, 0, buffer.Length)) > 0) {
            output.Write(buffer, 0, read);
        }
    }

}
}