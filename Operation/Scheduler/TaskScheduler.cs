using Operation.Comandos.Base;
using Quartz;
using Quartz.Impl;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Operation.Scheduler
{
    public class TaskScheduler
    {
        StdSchedulerFactory factory;    
       
        public void ScheduleTask(IComando comand)
        {

            IScheduler scheduler = StdSchedulerFactory.GetDefaultScheduler();

            IJobDetail job = CreateJob(comand);

            //TODO: Criar builder no domínio da nossa aplicação para Trigger.
            ITrigger trigger = TriggerBuilder.Create()
                .WithDailyTimeIntervalSchedule
                  (s =>
                     s.WithIntervalInHours(24)
                    .OnEveryDay()
                    .StartingDailyAt(TimeOfDay.HourAndMinuteOfDay(0, 0))
                  )
                .Build();

            scheduler.ScheduleJob(job, trigger);
        }
        

        private IJobDetail CreateJob(IComando comand)
        {
            IJobDetail job = JobBuilder.Create<ComandExecutionJob>()
                .Build();

            job.JobDataMap["comando"] = comand;

            return job;
        }
    }
}
