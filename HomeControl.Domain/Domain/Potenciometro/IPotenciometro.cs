using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Domain.Potenciometro
{
    interface IPotenciometro
    {
        void AumentarValor();
        void DiminuirValor();
        int GetValorAtual();
        void DiminuirParaValorMinimo();
        void AumentarParaValorMaximo();


    }
}
