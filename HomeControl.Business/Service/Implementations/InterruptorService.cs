using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Dispositivos;
using HomeControl.Domain.Interruptores;
using Operation;
using Operation.Comandos.Interruptores;
using Rest.Clients;
using System;
using System.Collections.Generic;

namespace HomeControl.Business.Service.Implementations
{
    public class InterruptorService : AbstractService<Interruptor, int>, IInterruptorService
    {

        private IInterruptorDao _interruptorDao;
        private IComodoService _comodoService;
        private IEmbarcadoService _embarcadoService;
        private DefaultDispositivoService _defaultdispositivo;

        public InterruptorService(IInterruptorDao interruptorDao, IComodoService comodoService, IEmbarcadoService embarcadoService, DefaultDispositivoService defaultDispositivo) : base(interruptorDao)
        {
            _interruptorDao = interruptorDao;
            _comodoService = comodoService;
            _embarcadoService = embarcadoService;
            _defaultdispositivo = defaultDispositivo;
        }

        public InterruptorService() : this(DaoFactory.GetInterruptorDao(), new ComodoService(), new EmbarcadoService(), new DefaultDispositivoService()) { }

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
            //TO DO: Registrar mudança de estado
            ComandoLigar comando = new ComandoLigar(new LigarInterruptorClient());
            comando.Dispositivo = dispositivo;

            ExecutorComando.Instance.Execute(comando);
            dispositivo.Estado = 1;
            Update(dispositivo);
        }

        public void DesligarDispositivo(Interruptor dispositivo)
        {
            //TO DO: Registrar mudança de estado
            ComandoLigar comando = new ComandoLigar(new LigarInterruptorClient());
            comando.Dispositivo = dispositivo;

            ExecutorComando.Instance.Execute(comando);
            dispositivo.Estado = 0;
            this.Update(dispositivo);
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

            if (entity.Porta == 0)
            {
                errors.Add("Informe uma porta válida");
            }
            else
            {
                List<Dispositivo> resul = _defaultdispositivo.FindByPorta(entity.Porta);

                if (resul != null && resul.Count > 0)
                {
                    errors.Add("A porta já está sendo utilizada por outro dispositivo");
                }
            }
            
            if (errors.HasErrors())
            {
                throw new BusinessException(errors);
            }


        }
    }
}
