using Operation.Comandos.Base;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Operation
{
    public class ExecutorComando
    {
        public static ExecutorComando _executorInstance;

        public static ExecutorComando Instance
        {
            get
            {
                if (_executorInstance == null)
                {
                    _executorInstance = new ExecutorComando();
                }

                return _executorInstance;
            }
        }

        public void Execute(IComando comando)
        {
            comando.Execute();
        }

    }
}
