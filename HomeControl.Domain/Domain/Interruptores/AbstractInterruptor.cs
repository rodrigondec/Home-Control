using HomeControl.Domain.Dispositivos;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace HomeControl.Domain.Interruptores
{
    public abstract class AbstractInterruptor : Dispositivo, Interruptor
    {
        public abstract void desligarDispositivo();

        public abstract bool getStatus();

        public abstract void ligarDispositivo();
    }
}