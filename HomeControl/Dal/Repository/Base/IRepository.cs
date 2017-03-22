using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Dal.Repository.Base
{
    interface IRepository<T, ID> where T: class
    {
        List<T> GetAll();
        T find(ID id);
        T update(T entity);
        void saveChanges();
        T add(T entity);
    }
}
