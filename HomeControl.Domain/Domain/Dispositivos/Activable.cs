using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Domain.Dispositivos
{
   public interface IActivable
    {
        void Activate();
        void Deactivate();
        Boolean IsActive();
    }
}
