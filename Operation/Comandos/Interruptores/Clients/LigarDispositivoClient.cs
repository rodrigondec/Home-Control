using System;
using HomeControl.Domain.Dispositivos;

namespace Operation.Comandos.Interruptores
{
    public class LigarInterruptorClient : ILigarInterruptorClient
    {
        public void LigarDispositivo(Dispositivo dispositivo)
        {

        }
        public void DesligarDispositivo(Dispositivo dispositivo)
        {
            
        }

        private string GetResourceLigarDispositivo(Dispositivo dispositivo)
        {
            return "";
        }
        
    }
}