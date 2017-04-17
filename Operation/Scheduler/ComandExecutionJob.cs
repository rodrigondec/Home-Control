using Operation.Comandos.Base;
using Quartz;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Operation.Scheduler
{
    public class ComandExecutionJob : IJob
    {
        public void Execute(IJobExecutionContext context)
        {
            IComando comando = (IComando) context.JobDetail.JobDataMap["comando"];
            comando.Execute();
        }
    }
}
