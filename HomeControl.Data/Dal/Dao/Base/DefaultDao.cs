using HomeControl.Domain;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Data.Dal.Dao.Base
{
    public class DefaultDao<T, PK> : AbstractDao<T, PK> where T : class, IPersistable<PK>
    {
        public DefaultDao(DbContext db) : base(db)
        {

        }
    }
}
