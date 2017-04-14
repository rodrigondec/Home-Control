using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Interruptores;
using System;
using System.Collections.Generic;

namespace HomeControl.Business.Service.Implementations
{
    public class InterruptorService : AbstractService<Interruptor, int>, IInterruptorService
    {

        private IInterruptorDao dao;

        public InterruptorService()
        {
            dao = DaoFactory.GetInterruptorDao();
            base.GenericDao = dao;
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

        public override void Validar(Interruptor entity)
        {
            ErrorList errors = new ErrorList();

            if(entity == null)
            {
                errors.Add("Interruptor não pode ser nulo");
                throw new BusinessException(errors);
            }

            if(entity.Comodo == null)
            {
                errors.Add("Necessário associar o dispositivo à um comodo.");
            }

            throw new BusinessException(errors);
           
        }
    }
}
