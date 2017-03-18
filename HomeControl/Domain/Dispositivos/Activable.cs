using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Domain.Dispositivos
{
   public interface Activable
    {
        void activate();
        void deactivate();
        Boolean isActive();
    }
}
