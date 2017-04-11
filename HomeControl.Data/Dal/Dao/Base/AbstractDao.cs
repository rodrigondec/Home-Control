using HomeControl.Dal.Repository.Base;
using HomeControl.Domain;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;

namespace HomeControl.Data.Dal.Dao.Base
{
    public abstract class AbstractDao<T, ID> : IGenericDao<T, ID>, ILinqDao<T>, IDisposable where T: class,IPersistable<ID>
    {

       protected DbContext db;

       public AbstractDao(DbContext db)
       {
            this.db = db;
       }

       public T Add(T entity)
        {
            entity = db.Set<T>().Add(entity);
            db.SaveChanges();
            return entity;
        }

        public T Find(ID id)
        {
            return db.Set<T>().Find(id);
        }

        public IEnumerable<T> FindAll(Func<T, bool> exp)
        {
            return db.Set<T>().Where(exp);
        }

        public T First(Func<T, bool> exp)
        {
            return db.Set<T>().First();
        }

        public List<T> FindAll()
        {
            return db.Set<T>().ToList();
        } 

        public void SaveChanges()
        {
            db.SaveChanges();
        }

        public T FindOne(Func<T, bool> exp)
        {
            return db.Set<T>().SingleOrDefault(exp);
        }

        public T Update(T entity)
        {
            if (entity == null)
                return null;

            T existing = Find(entity.Id);

            if (existing != null)
            {
                db.Entry(existing).CurrentValues.SetValues(entity);
                db.SaveChanges();
            }
            return existing;
        }

        public T Remove(T entity)
        {
            return null;
        }

        public void Dispose()
        {
            db.Dispose();
        }
    }
}
