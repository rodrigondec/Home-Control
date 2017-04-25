using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Dispositivos;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Implementations
{
    public class EmbarcadoService : AbstractService<Embarcado, int>, IEmbarcadoService
    {
        private IEmbarcadoDao _dao;

        public EmbarcadoService(IEmbarcadoDao embarcadoDao) : base(embarcadoDao)
        {
            _dao = embarcadoDao;
        }

        public EmbarcadoService() : this(DaoFactory.GetEmbarcadoDao()) { }

        public override Embarcado Add(Embarcado entity)
        {
            Validar(entity);
            return _dao.Add(entity);
        }

        public override void Dispose()
        {
            _dao.Dispose();
        }

        public override Embarcado Find(int id)
        {
            return _dao.Find(id);
        }

        public override List<Embarcado> FindAll()
        {
            return _dao.FindAll();
        }

        public override Embarcado Update(Embarcado entity)
        {
            Validar(entity);
            return _dao.Update(entity);
        }

        public override void Validar(Embarcado entity)
        {
            ErrorList erros = new ErrorList();

            if (entity == null)
            {
                erros.Add("O Embarcado precisa ser preenchido");
            }

            if (string.IsNullOrEmpty(entity.Nome))
            {
                erros.Add("Nome precisa ser preenchido");
            }

            if (string.IsNullOrEmpty(entity.MacAddress))
            {
                erros.Add("Mac Address precisar ser preenchido");
            }

            if (string.IsNullOrEmpty(entity.Socket))
            {
                erros.Add("IP precisar ser preenchido");
            }
            
            if (erros.HasErrors())
            {
                throw new BusinessException(erros);
            }
        }
    }
}
