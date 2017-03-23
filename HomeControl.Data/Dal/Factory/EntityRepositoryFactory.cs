using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Repository.Custom.Implementations;
using HomeControl.Data.Dal.Repository.Custom.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Data.Dal.Factory
{
    public class EntityRepositoryFactory : RepositoryFactory
    {
        private HomeControlDBContext db;
        public EntityRepositoryFactory(HomeControlDBContext db)
        {
            this.db = db;
        }

        public override IComodoRepository getComodoRepository()
        {
            return new ComodoRepository(db);
        }

        public override IControladorRepository getControladorRepository()
        {
            return new ControladorRepository(db);
        }

        public override IDispositivoRepository getDispositivoRepository()
        {
            return new DispositivoRepository(db);
        }

        public override IResidenciaRepository getResidenciaRepository()
        {
            return new ResidenciaRepository(db);
        }

    }
}
