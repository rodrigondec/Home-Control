using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Operation.Comandos.Base
{
    public interface IComando
    {
        void Execute();
        void UnExecute();

    }
}
