using HomeControl.Business.Service.Base.interfaces;
using HomeControl.Business.Service.Configuration;
using HomeControl.Data.Dal.Factory;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Implementation
{
    public abstract class AbstractService<T, PK> : ICrudService<T, PK> where T : class
    {
        public abstract T Add(T entity);
        public abstract void Dispose();
        public abstract T Find(PK id);
        public abstract List<T> FindAll();
        public abstract T Update(T entity);

        protected static DaoFactory GetDaoFactory()
        {
            return DalConfiguration.GetDaoFactory();
        }
    }
}
