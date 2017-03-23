using HomeControl.Data.Dal.Repository.Base;
using System.Data.Entity;
using HomeControl.Domain.Residencia;
using HomeControl.Data.Dal.Repository.Custom.Interfaces;
using HomeControl.Data.Dal.Context;

namespace HomeControl.Data.Dal.Repository.Custom.Implementations
{
    public class ComodoRepository : AbstractRepository<Comodo, int>, IComodoDao
    {
        public ComodoRepository(HomeControlDBContext db) : base(db)
        {
            
        }

    }
}
