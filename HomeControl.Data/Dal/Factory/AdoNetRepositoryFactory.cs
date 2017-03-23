using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using HomeControl.Data.Dal.Repository.Custom.Interfaces;

namespace HomeControl.Data.Dal.Factory
{
    public class AdoNetRepositoryFactory : RepositoryFactory
    {
        public override IComodoRepository getComodoRepository()
        {
            return null;
        }

        public override IControladorRepository getControladorRepository()
        {
            return null;
        }

        public override IDispositivoRepository getDispositivoRepository()
        {
            return null;
        }

        public override IResidenciaRepository getResidenciaRepository()
        {
            return null;
        }
    }
}
