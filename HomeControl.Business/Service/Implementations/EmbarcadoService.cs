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
        private IEmbarcadoDao dao;

        public EmbarcadoService()
        {            
            dao = DaoFactory.GetEmbarcadoDao();
            base.GenericDao = dao;
        }

        public override Embarcado Add(Embarcado entity)
        {
            Validar(entity);
            return dao.Add(entity);
        }

        public override void Dispose()
        {
            dao.Dispose();
        }

        public override Embarcado Find(int id)
        {
            return dao.Find(id);
        }

        public override List<Embarcado> FindAll()
        {
            return dao.FindAll();
        }

        public override Embarcado Update(Embarcado entity)
        {
            Validar(entity);
            return dao.Update(entity);
        }

        public override void Validar(Embarcado entity)
        {
            ErrorList erros = new ErrorList();

            if (entity == null)
            {
                erros.Add("O Embarcado precisa ser preenchido");
            }

            if (entity.MacAddress == "")
            {
                erros.Add("Mac Address precisar ser preenchido");
            }

            if (entity.IpAddress == "")
            {
                erros.Add("IP precisar ser preenchido");
            }

            if(entity.Nome == "")
            {
                erros.Add("Nome precisa ser preenchido");
            }

            if (erros.HasErrors())
            {
                throw new BusinessException(erros);
            }
        }
    }
}
