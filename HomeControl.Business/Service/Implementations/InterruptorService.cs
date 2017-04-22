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
        private IComodoService _comodoService;
        private IEmbarcadoService _embarcadoService;

        public InterruptorService(IInterruptorDao interruptorDao, IComodoService comodoService, IEmbarcadoService embarcadoService) : base(interruptorDao)
        {
            _interruptorDao = interruptorDao;
            _comodoService = comodoService;
            _embarcadoService = embarcadoService;
        }

        public InterruptorService()
        {
            _interruptorDao = DaoFactory.GetInterruptorDao();
            _comodoService = new ComodoService();
            _embarcadoService = new EmbarcadoService();
        }


        public override Interruptor Add(Interruptor entity)
        {
            if (entity.Id > 0)
            {
                throw new BusinessException("Não é possível criar um Interruptor já existente.");
            }

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

            if (entity == null)
            {
                errors.Add("Interruptor não pode ser nulo");
                throw new BusinessException(errors);
            }
            
            if (_comodoService.Find(entity.ComodoId) == null)
            {
                errors.Add("Necessário associar o dispositivo à um comodo.");
            }


            if (_embarcadoService.Find(entity.Embarcadoid) == null)
            {
                errors.Add("Necessário associar a um Embarcado");
            }

            if(entity.Porta == 0)
            {
                errors.Add("Informe uma porta válida");
            }

            if (errors.HasErrors())
            {
                throw new BusinessException(errors);
            }


        }
    }
}
