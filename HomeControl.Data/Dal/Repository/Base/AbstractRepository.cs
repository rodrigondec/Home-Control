using HomeControl.Dal.Repository.Base;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;

namespace HomeControl.Data.Dal.Repository.Base
{
    public abstract class AbstractRepository<T, ID> : IRepository<T, ID>, LinqRepository<T> where T: class
    {

       protected DbContext db;

       public AbstractRepository(DbContext db)
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

            T existing = db.Set<T>().Find(entity);
            if (existing != null)
            {
                db.Entry(existing).CurrentValues.SetValues(entity);
                db.SaveChanges();
            }
            return existing;
        }
    }
}
