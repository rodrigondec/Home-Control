using HomeControl.Business.Service.Base.interfaces;
using HomeControl.Business.Service.Configuration;
using HomeControl.Dal.Repository.Base;
using HomeControl.Data.Dal.Factory;
using HomeControl.Domain;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Implementations
{
    public abstract class AbstractService<T, PK> : ICrudService<T, PK> where T : class, IPersistable<PK>
    {
        IGenericDao<T, PK> genericDao;

        public abstract T Add(T entity);
        public abstract void Dispose();
        public abstract T Find(PK id);
        public abstract List<T> FindAll();
        public abstract T Update(T entity);
        protected abstract void Validar(T entity);
        public T Remove(T entity)
        {
          return genericDao.Remove(entity);
        }
        public static DaoFactory DaoFactory
        {
            get
            {
                return DalConfiguration.GetDaoFactory();
            }
        }
    }
    
}

