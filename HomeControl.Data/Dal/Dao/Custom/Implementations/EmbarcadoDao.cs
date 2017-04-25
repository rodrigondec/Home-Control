using HomeControl.Data.Dal.Dao.Base;
using HomeControl.Domain.Dispositivos;
using System.Data.Entity;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Data.Dal.Context;
using System.Collections.Generic;

namespace HomeControl.Data.Dal.Dao.Custom.Implementations
{
    public class EmbarcadoDao : AbstractDao<Embarcado, int>, IEmbarcadoDao
    {
        public EmbarcadoDao(HomeControlDBContext db) : base(db)
        {
        }

        public List<Embarcado>FindByPorta(int porta)
        {

            return null;
        }
    }
}
