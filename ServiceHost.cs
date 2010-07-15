using System;
using System.ServiceModel;
using System.ServiceModel.Web;

namespace LWebService {
public class ServiceHostMainProg {
    static public void Main() {
        var host = new WebServiceHost(typeof(LicensewebService), new Uri("http://localhost:8000/"));
        var ep = host.AddServiceEndpoint(typeof(ILicensewebService), new WebHttpBinding(), "");
        host.Open();
        Console.WriteLine("Service running, press enter to quit");
        Console.ReadLine();
        host.Close();
    }
}
}