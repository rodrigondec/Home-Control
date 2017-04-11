using HomeControl.Domain.Dispositivos;
using System;

namespace HomeControl.Domain.Interruptores
{
    public class Interruptor : Dispositivo, IInterruptor
    {
        public override void Activate()
        {
            throw new NotImplementedException();
        }

        public override void Deactivate()
        {
            throw new NotImplementedException();
        }

        public void DesligarDispositivo()
        {
        }

        public bool GetStatus()
        {
            //TO DO: Implementar retorno do status real
            return true;
        }

        public override bool IsActive()
        {
            throw new NotImplementedException();
        }

        public void LigarDispositivo() { }
    }
}