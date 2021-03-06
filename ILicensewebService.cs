﻿using System.ServiceModel;
using System.ServiceModel.Web;
using System.IO;

namespace LWebService {

[ServiceContract]
public interface ILicensewebService {
    [OperationContract]
    [WebGet]
    string AuthenticateUser(string username, string password);

    [OperationContract]
    [WebInvoke]
    Stream DownloadMetadata(Stream search);
    
    [OperationContract]
    [WebGet]
    Stream DownloadFile(string token, string objectID, int version, bool rendition, string renditionType);

    [OperationContract]
    [WebInvoke]
    string UploadMetadata(Stream metadata);
    
    [OperationContract]
    [WebInvoke(UriTemplate="UploadFile?token={token}&contextID={contextID}")]
    string UploadFile(Stream content, string token, string contextID);    
    
}

}