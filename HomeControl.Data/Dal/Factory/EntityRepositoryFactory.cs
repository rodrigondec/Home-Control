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
    public class EntityRepositoryFactory : DaoFactory
    {
        private HomeControlDBContext db;
        public EntityRepositoryFactory(HomeControlDBContext db)
        {
            this.db = db;
        }

        public override IComodoDao getComodoRepository()
        {
            return new ComodoRepository(db);
        }

        public override IControladorDao getControladorRepository()
        {
            return new ControladorRepository(db);
        }

        public override IDispositivoDao getDispositivoRepository()
        {
            return new DispositivoRepository(db);
        }

        public override IResidenciaDao getResidenciaRepository()
        {
            return new ResidenciaRepository(db);
        }

    }
}
