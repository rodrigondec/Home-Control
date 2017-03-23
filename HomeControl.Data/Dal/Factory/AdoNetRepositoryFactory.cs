using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using HomeControl.Data.Dal.Repository.Custom.Interfaces;

namespace HomeControl.Data.Dal.Factory
{
    public class AdoNetRepositoryFactory : DaoFactory
    {
        public override IComodoDao getComodoDao()
        {
            return null;
        }

        public override IControladorDao getControladorDao()
        {
            return null;
        }

        public override IDispositivoDao getDispositivoDao()
        {
            return null;
        }

        public override IResidenciaDao getResidenciaDao()
        {
            return null;
        }
    }
}
