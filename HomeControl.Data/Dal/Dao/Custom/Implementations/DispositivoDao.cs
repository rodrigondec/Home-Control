using HomeControl.Data.Dal.Dao.Base;
using HomeControl.Domain.Dispositivos;
using System.Data.Entity;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Data.Dal.Context;
using System.Collections.Generic;
using System.Linq;

namespace HomeControl.Data.Dal.Dao.Custom.Implementations
{
    public class DispositivoDao : AbstractDao<Dispositivo, int>, IDispositivoDao
    {
        private HomeControlDBContext _db;

        public DispositivoDao(HomeControlDBContext db) : base(db)
        {
            _db = db;
        }

        public List<Dispositivo> FindByPorta(int porta)
        {
            IQueryable<Dispositivo> query = from Dispositivo dispositivo in _db.Dispositivos
                        where dispositivo.Porta == porta
                        select dispositivo;

            return query.ToList();
        }
    }
}
