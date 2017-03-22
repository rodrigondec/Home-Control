using HomeControl.Data.Dal.Repository.Base;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.Entity;
using HomeControl.Domain.Residencia;
using HomeControl.Data.Dal.Repository.Interfaces;

namespace HomeControl.Data.Dal.Repository.Implementations
{
    public class ComodoRepository : AbstractRepository<Comodo, int>, IComodoRepository
    {
        public ComodoRepository(DbContext db) : base(db)
        {
            
        }

    }
}
