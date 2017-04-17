using HomeControl.Domain.Dispositivos;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Operation.Comandos.Base
{
    public abstract class ComandoAbstrato<T> : IComando where T : Dispositivo
    {
        public T Dispositivo { get; set; }

        public abstract void Execute();
        public abstract void UnExecute();

    }
}
