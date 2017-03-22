using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Dal.Repository.Base
{
    interface IRepository<T, ID> where T: class
    {
        List<T> FindAll();
        T Find(ID id);
        T Update(T entity);
        void SaveChanges();
        T Add(T entity);
    }
}
