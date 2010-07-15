using System.IO;
namespace LWebService {

public interface ILiveLinkFacade {
    string GetLoginToken(string username, string password);
    Stream GetFile(string token, string objectID, int version, bool rendition, string renditionType);
}

}