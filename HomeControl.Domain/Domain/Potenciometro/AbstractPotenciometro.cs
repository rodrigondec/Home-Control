using HomeControl.Domain.Dispositivos;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace HomeControl.Domain.Potenciometro
{
    public abstract class AbstractPotenciometro : Dispositivo, IPotenciometro
    {
        
        private float valorAtual;
        private float valorMaximo;
        private float valorMinimo;
        private float estadoAtual;

        public abstract void AumentarParaValorMaximo();
        public abstract void AumentarValor();
        public abstract void DiminuirParaValorMinimo();
        public abstract void DiminuirValor();
        public abstract float GetValorAtual();
    }
}