using System;
using System.Collections.Generic;

namespace HomeControl.Data.Dal.Dao.Base
{
    interface ILinqDao<T> 
    {
        IEnumerable<T> FindAll(Func<T, bool> exp);           
        T FindOne(Func<T, bool> exp);
        T First(Func<T, bool> exp);
    }
}
