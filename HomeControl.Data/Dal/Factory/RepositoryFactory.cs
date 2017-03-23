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

        public abstract IComodoDao getComodoRepository(); 
        public abstract IControladorDao getControladorRepository(); 
        public abstract IDispositivoDao getDispositivoRepository();
        public abstract IResidenciaDao getResidenciaRepository();

    }
}
