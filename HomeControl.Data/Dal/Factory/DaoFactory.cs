using HomeControl.Data.Dal.Repository.Custom.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Data.Dal.Factory
{
    public abstract class DaoFactory
    {

        public abstract IComodoDao getComodoDao(); 
        public abstract IControladorDao getControladorDao(); 
        public abstract IDispositivoDao getDispositivoDao();
        public abstract IResidenciaDao getResidenciaDao();

    }
}
