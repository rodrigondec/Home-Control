using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Data.Dal.Repository.Base
{
    interface LinqRepository<T> where T : class
    {
        IEnumerable<T> FindAll(Func<T, bool> exp);           
        T FindOne(Func<T, bool> exp);
        T First(Func<T, bool> exp);
    }
}
