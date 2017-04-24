using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Domain.Interruptores
{
    public interface IInterruptor
    {
        bool GetStatus();
        void DesligarDispositivo();
        void LigarDispositivo();
    }
}
