using HomeControl.Data.Dal.Dao.Base;
using HomeControl.Domain.Dispositivos;
using System.Data.Entity;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Data.Dal.Context;

namespace HomeControl.Data.Dal.Dao.Custom.Implementations
{
    public class DispositivoDao : AbstractDao<Dispositivo, int>, IDispositivoDao
    {
        public DispositivoDao(HomeControlDBContext db) : base(db)
        {

        }
    }
}
