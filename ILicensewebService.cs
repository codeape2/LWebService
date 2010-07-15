using System.ServiceModel;
using System.ServiceModel.Web;

namespace LWebService {

[ServiceContract]
public interface ILicensewebService {
    [OperationContract]
    [WebGet]
    string AuthenticateUser(string username, string password);
}
}