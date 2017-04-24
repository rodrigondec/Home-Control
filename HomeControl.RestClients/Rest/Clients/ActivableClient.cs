using Rest.Clients;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Rest.Clients
{
    public class ActivableClient : BaseClient
    {
        public void Activate(String ipAddress,int porta)
        {
            GetResultSynchronously(GetResourceActivate(ipAddress, porta));
        }
        public void Deactivate(String ipAddress, int porta)
        {
            GetResultSynchronously(GetResourceDeactivate(ipAddress, porta));
        }

        #region Resources
        public string GetResourceActivate(String ipAddress, int porta)
        {
            String dominio = ipAddress;
            String acao = "Activate";           

            return dominio+"/"+acao+"/"+porta;
        }
        public string GetResourceDeactivate(String ipAddress, int porta)
        {
            String dominio = ipAddress;
            String acao = "Activate";

            return dominio + "/" + acao + "/" + porta;
        }
        #endregion
    }
}
