using HomeControl.Data.Dal.Dao.Base;
using HomeControl.Domain.Dispositivos;
using System.Data.Entity;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Data.Dal.Context;
using System.Collections.Generic;

namespace HomeControl.Data.Dal.Dao.Custom.Implementations
{
    public class DispositivoDao : AbstractDao<Dispositivo, int>, IDispositivoDao
    {
        public DispositivoDao(HomeControlDBContext db) : base(db)
        {

        }

        public List<Dispositivo> FindByPorta(int porta)
        {
             return FindAll(x => x.Porta == porta) as List<Dispositivo>; 
        }
    }
}
