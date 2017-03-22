using HomeControl.Data.Dal.Repository.Base;
using System.Data.Entity;
using HomeControl.Domain.Residencia;
using HomeControl.Data.Dal.Repository.Custom.Interfaces;

namespace HomeControl.Data.Dal.Repository.Custom.Implementations
{
    public class ComodoRepository : AbstractRepository<Comodo, int>, IComodoRepository
    {
        public ComodoRepository(DbContext db) : base(db)
        {
            
        }

    }
}
