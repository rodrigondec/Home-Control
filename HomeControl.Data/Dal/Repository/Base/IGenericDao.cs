using System;
using System.Collections.Generic;

namespace HomeControl.Dal.Repository.Base
{
    public interface IGenericDao<T, ID> : IDisposable where T: class
    {
        List<T> FindAll();
        T Find(ID id);
        T Update(T entity);
        void SaveChanges();
        T Add(T entity);
    }
}
