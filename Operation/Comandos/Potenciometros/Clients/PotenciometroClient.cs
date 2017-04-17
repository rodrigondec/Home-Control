

using HomeControl.Domain.Potenciometro;

namespace Operation.Comandos.Potenciometros.Clients
{
    public interface PotenciometroClient
    {        
        void AumentarValor(AbstractPotenciometro potenciometro,float valor);
        void DiminuirValor(AbstractPotenciometro potenciometro, float valor);
        float RecuperarValorAtual(AbstractPotenciometro potenciometro);
        void DimininuirParaValorMinimo(AbstractPotenciometro potenciometro);
        void AumentarParaValorMaximo(AbstractPotenciometro potenciometro);
    }
}
