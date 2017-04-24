using Rest.Clients;
using System;
using HomeControl.Domain.Potenciometro;


namespace Rest.Clients
{
    public class PotenciometroClient : BaseClient, IPotenciometroClient
    {
        public PotenciometroClient() : base() { }

        public void AumentarParaValorMaximo(AbstractPotenciometro potenciometro)
        {
            GetResultSynchronously(GetResourceAlterarValor(potenciometro,potenciometro.ValorMaximo));
        }

        public void AumentarValor(AbstractPotenciometro potenciometro, float valor)
        {
            GetResultSynchronously(GetResourceAlterarValor(potenciometro,valor));
        }      

        public void DimininuirParaValorMinimo(AbstractPotenciometro potenciometro)
        {
            GetResultSynchronously(GetResourceAlterarValor(potenciometro, potenciometro.ValorMinimo));
        }

        public void DiminuirValor(AbstractPotenciometro potenciometro, float valor)
        {
            GetResultSynchronously(GetResourceAlterarValor(potenciometro, valor));
        }

        public float RecuperarValorAtual(AbstractPotenciometro potenciometro)
        {
            ValorDTO valor = DesserializeContent<ValorDTO>(GetResultSynchronously(GetResourceRecuperarValor(potenciometro)));

            if(valor == null)
            {
                throw new RestClientException("Erro ao recuperar valor atual do sensor.");
            }

            return (float) valor.Valor;
        }

        #region Resources    
        private string GetResourceAlterarValor(AbstractPotenciometro potenciometro, float valor)
        {
            String dominio = potenciometro.Embarcado.IpAddress;
            String acao = "AlterarValorPotenciometro";
            int porta = potenciometro.Porta;

            return dominio + "/" + acao + "/" + porta+"/"+valor;
        }

        private string GetResourceRecuperarValor(AbstractPotenciometro potenciometro)
        {
            String dominio = potenciometro.Embarcado.IpAddress;
            String acao = "ResourceRecuperarValor";
            int porta = potenciometro.Porta;

            return dominio + "/" + acao + "/" + porta;
        }
        #endregion
    }
}
