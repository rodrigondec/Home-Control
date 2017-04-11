using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Domain.Interruptores
{
    interface IInterruptor
    {
        bool GetStatus();
        void DesligarDispositivo();
        void LigarDispositivo();
    }
}
