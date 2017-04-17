using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Interruptores;
using Operation;
using Operation.Comandos.Interruptores;
using System;
using System.Collections.Generic;

namespace HomeControl.Business.Service.Implementations
{
    public class InterruptorService : AbstractService<Interruptor, int>, IInterruptorService
    {

        private IInterruptorDao _interruptorDao;
        public InterruptorService(IInterruptorDao interruptorDao) : base(interruptorDao)
        {
            _interruptorDao = interruptorDao;            
        }
        public InterruptorService() :  this(DaoFactory.GetInterruptorDao()){}

        public override Interruptor Add(Interruptor entity)
        {
            Validar(entity);
            return _interruptorDao.Add(entity);
        }

        public override void Dispose()
        {
            _interruptorDao.Dispose();
        }

        public override Interruptor Find(int id)
        {
            return _interruptorDao.Find(id);
        }

        public override List<Interruptor> FindAll()
        {
            return _interruptorDao.FindAll();
        }

        public override Interruptor Update(Interruptor entity)
        {
            Validar(entity);
            return _interruptorDao.Update(entity);
        }

        public void LigarDispositivo(Interruptor dispositivo)
        {
            ComandoLigar comando = new ComandoLigar(new LigarInterruptorClient());
            comando.Dispositivo = dispositivo;

            ExecutorComando.Instance.Execute(comando);
        }
        public void DesligarDispositivo(Interruptor dispositivo)
        {
            ComandoLigar comando = new ComandoLigar(new LigarInterruptorClient());
            comando.Dispositivo = dispositivo;

            ExecutorComando.Instance.Execute(comando);
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
