using HomeControl.Data.Dal.Repository.Custom.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Data.Dal.Factory
{
    public abstract class RepositoryFactory
    {

        public abstract IComodoRepository getComodoRepository(); 
        public abstract IControladorRepository getControladorRepository(); 
        public abstract IDispositivoRepository getDispositivoRepository();
        public abstract IResidenciaRepository getResidenciaRepository();

    }
}
