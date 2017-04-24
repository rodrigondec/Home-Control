using System;
using HomeControl.Domain.Dispositivos;
using System.Net;
using System.IO;
using System.Text;
using System.Runtime.Serialization.Json;
using System.Net.Http;
using Rest.Clients;
using HomeControl.RestClients.Rest.Clients;
using HomeControl.Domain.Interruptores;

namespace Rest.Clients
{
    public class LigarInterruptorClient : BaseClient, ILigarInterruptorClient
    {

        private HttpClient client;

        public LigarInterruptorClient()
        {
            client = new HttpClient();
        }

        public void LigarDispositivo(Interruptor dispositivo)
        {
            GetResultSynchronously(GetResourceLigarDispositivo(dispositivo));
        }

        public void DesligarDispositivo(Interruptor dispositivo)
        {
            GetResultSynchronously(GetResourceDesligarDispositivo(dispositivo));
        }

        public bool GetStatusInterruptor(Interruptor interruptor)
        {
            StatusDTO statusInterrruptor = DesserializeContent<StatusDTO>(GetResultSynchronously(GetResourceStatusInterruptor(interruptor)));

            if (statusInterrruptor == null)
            {
                throw new RestClientException("");
            }

            return statusInterrruptor.Status;
        }


        private string GetResourceLigarDispositivo(Dispositivo dispositivo)
        {

            String dominio = dispositivo.Embarcado.IpAddress;
            int portaDispositivo = dispositivo.Porta;
            String acao = "Ligar";

            return dominio + "/" + acao + "/" + portaDispositivo;

        }

        private string GetResourceDesligarDispositivo(Dispositivo dispositivo)
        {

            String dominio = dispositivo.Embarcado.IpAddress;
            int portaDispositivo = dispositivo.Porta;
            String acao = "Desligar";

            return dominio + "/" + acao + "/" + portaDispositivo;

        }

        private string GetResourceStatusInterruptor(Interruptor dispositivo)
        {
            String dominio = dispositivo.Embarcado.IpAddress;
            int portaDispositivo = dispositivo.Porta;
            String acao = "Status";

            return dominio + "/" + acao + "/" + portaDispositivo;
        }


    }
}