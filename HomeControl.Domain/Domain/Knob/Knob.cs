using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Domain.Knob
{
    interface Knob
    {
        void aumentarValor();
        void diminuirValor();
        int getValorAtual();
        void diminuirParaValorMinimo();
        void aumentarParaValorMaximo();


    }
}
