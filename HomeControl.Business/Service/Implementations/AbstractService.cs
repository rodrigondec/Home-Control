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

        protected IGenericDao<T, PK> GenericDao { get; set; }

        public AbstractService(IGenericDao<T, PK> genericDao)
        {
            this.GenericDao = genericDao;
        }

        public AbstractService() { }

        public virtual T Add(T entity)
        {
            Validar(entity);
            return GenericDao.Add(entity);
        }
        public virtual T Find(PK id)
        {
            return GenericDao.Find(id);
        }
        public virtual List<T> FindAll()
        {
            return GenericDao.FindAll();
        }
        public virtual T Update(T entity)
        {
            Validar(entity);
            return GenericDao.Update(entity);
        }
        public abstract void Validar(T entity);
        public T Remove(T entity)
        {
            return GenericDao.Remove(entity);
        }
        public virtual void Dispose()
        {
            GenericDao.Dispose();
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

