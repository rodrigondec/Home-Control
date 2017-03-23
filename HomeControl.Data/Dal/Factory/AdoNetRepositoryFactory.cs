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
        public override IComodoDao getComodoRepository()
        {
            return null;
        }

        public override IControladorDao getControladorRepository()
        {
            return null;
        }

        public override IDispositivoDao getDispositivoRepository()
        {
            return null;
        }

        public override IResidenciaDao getResidenciaRepository()
        {
            return null;
        }
    }
}
