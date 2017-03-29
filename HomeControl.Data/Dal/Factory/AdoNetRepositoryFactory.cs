using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;

namespace HomeControl.Data.Dal.Factory
{
    public class AdoNetRepositoryFactory : DaoFactory
    {
        public override IComodoDao GetComodoDao()
        {
            return null;
        }

        public override IControladorDao GetControladorDao()
        {
            return null;
        }

        public override IDispositivoDao GetDispositivoDao()
        {
            return null;
        }

        public override IInterruptorDao GetInterruptorDao()
        {
            return null;
        }

        public override IResidenciaDao GetResidenciaDao()
        {
            return null;
        }

        public override ISensorDao GetSensorDao()
        {
            return null;
        }
    }
}
