using HomeControl.Domain.Dispositivos;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace HomeControl.Domain.Potenciometro
{
    public abstract class AbstractPotenciometro : Dispositivo, IPotenciometro
    {        
        public float ValorAtual { get; set; }
        public float ValorMaximo { get; set; }
        public float ValorMinimo { get; set; }
        public float EstadoAtual { get; set; }

        public abstract void AumentarParaValorMaximo();
        public abstract void AumentarValor();
        public abstract void DiminuirParaValorMinimo();
        public abstract void DiminuirValor();
        public abstract float GetValorAtual();
    }
}