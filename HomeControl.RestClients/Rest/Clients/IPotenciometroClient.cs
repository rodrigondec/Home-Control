

using HomeControl.Domain.Potenciometro;

namespace Rest.Clients
{
    public interface IPotenciometroClient
    {        
        void AumentarValor(AbstractPotenciometro potenciometro,float valor);
        void DiminuirValor(AbstractPotenciometro potenciometro, float valor);
        float RecuperarValorAtual(AbstractPotenciometro potenciometro);
        void DimininuirParaValorMinimo(AbstractPotenciometro potenciometro);
        void AumentarParaValorMaximo(AbstractPotenciometro potenciometro);
    }
}
