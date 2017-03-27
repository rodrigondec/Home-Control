using HomeControl.Domain.Dispositivos;
using System;

namespace HomeControl.Domain.Interruptores
{
    public class Interruptor : Dispositivo, IInterruptor
    {
        public override void activate()
        {
            throw new NotImplementedException();
        }

        public override void deactivate()
        {
            throw new NotImplementedException();
        }

        public void desligarDispositivo()
        {
        }

        public bool getStatus()
        {
            //TO DO: Implementar retorno do status real
            return true;
        }

        public override bool isActive()
        {
            throw new NotImplementedException();
        }

        public void ligarDispositivo() { }
    }
}