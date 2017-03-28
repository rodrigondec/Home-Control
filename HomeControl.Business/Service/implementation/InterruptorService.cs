using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Interruptores;
using System;
using System.Collections.Generic;

namespace HomeControl.Business.Service.Implementation
{
    public class InterruptorService : AbstractService<Interruptor, int>
    {

        private IInterruptorDao dao;

        public InterruptorService()
        {
            dao = daoFactory.GetInterruptorDao();
        }

        public override Interruptor Add(Interruptor entity)
        {
            Validar(entity);
            return dao.Add(entity);
        }

        public override void Dispose()
        {
            dao.Dispose();
        }

        public override Interruptor Find(int id)
        {
            return dao.Find(id);
        }

        public override List<Interruptor> FindAll()
        {
            return dao.FindAll();
        }

        public override Interruptor Update(Interruptor entity)
        {
            Validar(entity);
            return dao.Update(entity);
        }

        protected override void Validar(Interruptor entity)
        {
            //to do: Validações
            throw new NotImplementedException();
        }
    }
}
