using System.ServiceModel;
using System.ServiceModel.Web;
using System.IO;

namespace LWebService {

[ServiceContract]
public interface ILicensewebService {
    [OperationContract]
    [WebGet]
    string AuthenticateUser(string username, string password);
    
    [OperationContract]
    [WebGet]
    Stream DownloadFile(string token, string objectID, int version, bool rendition, string renditionType);
}
}