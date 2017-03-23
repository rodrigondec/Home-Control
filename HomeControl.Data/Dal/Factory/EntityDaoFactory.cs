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
    public class EntityDaoFactory : DaoFactory
    {
        private HomeControlDBContext db;
        public EntityDaoFactory(HomeControlDBContext db)
        {
            this.db = db;
        }

        public override IComodoDao getComodoDao()
        {
            return new ComodoRepository(db);
        }

        public override IControladorDao getControladorDao()
        {
            return new ControladorRepository(db);
        }

        public override IDispositivoDao getDispositivoDao()
        {
            return new DispositivoRepository(db);
        }

        public override IResidenciaDao getResidenciaDao()
        {
            return new ResidenciaRepository(db);
        }

    }
}
