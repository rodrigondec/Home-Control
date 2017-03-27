using HomeControl.Data.Dal.Dao.Base;
using System.Data.Entity;
using HomeControl.Domain.Residencia;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Data.Dal.Context;

namespace HomeControl.Data.Dal.Dao.Custom.Implementations
{
    public class ComodoDao : AbstractDao<Comodo, int>, IComodoDao
    {
        public ComodoDao(HomeControlDBContext db) : base(db)
        {
            
        }

    }
}
