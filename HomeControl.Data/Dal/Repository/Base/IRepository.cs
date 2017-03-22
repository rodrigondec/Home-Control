using System.Collections.Generic;

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
