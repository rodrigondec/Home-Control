using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
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

        public override IComodoDao GetComodoDao()
        {
            return new ComodoDao(db);
        }

        public override IEmbarcadoDao GetControladorDao()
        {
            return new EmbarcadoDao(db);
        }

        public override IDispositivoDao GetDispositivoDao()
        {
            return new DispositivoDao(db);
        }

        public override IInterruptorDao GetInterruptorDao()
        {
            return new InterruptorDao(db);
        }

        public override ISensorDao GetSensorDao()
        {
            return new SensorDao(db);
        }

        public override IResidenciaDao GetResidenciaDao()
        {
            return new ResidenciaDao(db);
        }

    }
}
