using HomeControl.Business.Service.Implementations;
using HomeControl.Business.Service.Interfaces;
using Ninject.Modules;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Configuration
{
    public class BusinessNinjectModule : NinjectModule
    {
        public override void Load()
        {
            Bind<IComodoService>().To<ComodoService>();
            Bind<IEmbarcadoService>().To<EmbarcadoService>();
            Bind<IHistoricoUsoDispositivoService>().To<HistoricoUsoDispositivoService>();
            Bind<IInterruptorService>().To<InterruptorService>();            
            Bind<IResidenciaService>().To<ResidenciaService>();
            Bind<ISensorService>().To<SensorService>();
        }
    }
}
