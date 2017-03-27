using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Interruptores;
using System;
using System.Collections.Generic;

namespace HomeControl.Business.Service.Implementation
{
    public class InterruptorService : AbstractService<Interruptor, int>
    {
        private IDispositivoDao dao;

        public InterruptorService()
        {
            dao = daoFactory.GetDispositivoDao();
        }

        public override Interruptor Add(Interruptor entity)
        {
            return dao.Add(entity);
        }

        public override void Dispose()
        {
            throw new NotImplementedException();
        }

        public override Interruptor Find(int id)
        {
            throw new NotImplementedException();
        }

        public override List<Interruptor> FindAll()
        {
            throw new NotImplementedException();
        }

        public override Interruptor Update(Interruptor entity)
        {
            throw new NotImplementedException();
        }
    }
}
