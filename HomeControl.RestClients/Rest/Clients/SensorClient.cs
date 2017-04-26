using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using HomeControl.Domain.Sensores;
using Rest.Clients;


namespace Rest.Clients
{
    public class SensorClient : BaseClient, ISensorClient
    {
        private static SensorClient _instance = new SensorClient();
        public static SensorClient Instance { get { return _instance; }}

        private SensorClient(): base() {}

        public double RecuperarValorAtual(Sensor sensor)
        {

            string v = GetResultSynchronously(GetResourceRecuperarValorAtual(sensor));
            ValorDTO valorDTO = DesserializeContent<ValorDTO>(v);            

            if (valorDTO == null)
            {
                throw new RestClientException("Erro ao recuperar valor de sensor");
            }

            return valorDTO.Valor;

        }

        private string GetResourceRecuperarValorAtual(Sensor sensor)
        {
            String dominio = sensor.Embarcado.Socket;
            String acao = "VALORATUALSENSOR";
            int porta = sensor.Porta;

            return "http://"+dominio+"/"+acao;
        }

    }
}
