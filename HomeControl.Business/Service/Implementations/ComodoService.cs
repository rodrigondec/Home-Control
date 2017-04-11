using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Base.interfaces;
using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Factory;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Residencia;
using System;
using System.Collections.Generic;
using HomeControl.Business.Service.Interfaces;

namespace HomeControl.Business.Service.Implementations
{
    /// <summary>
    /// Serviço cuja finalidade é gerenciar os comodos de uma residência. 
    /// </summary>
    public class ComodoService : AbstractService<Comodo, int>, IComodoService
    {
        private IComodoDao _dao;

        public ComodoService()
        {
            _dao = DaoFactory.GetComodoDao();
        }

        public override Comodo Add(Comodo entity)
        {
            Validar(entity);

            return _dao.Add(entity);
        }

        public override void Dispose()
        {
            base.Dispose();
            _dao.Dispose();
        }

        public override Comodo Find(int id)
        {
            return _dao.Find(id);
        }

        public override List<Comodo> FindAll()
        {
            return _dao.FindAll();
        }

        public override Comodo Update(Comodo entity)
        {
            Validar(entity);
            return _dao.Update(entity);
        }

        protected override void Validar(Comodo entity)
        {
            ErrorList erros = new ErrorList();

            if (entity == null)
            {
                erros.Add("Comodo precisa ser Preenchido");
            }

            if(entity.Residencia == null)
            {
                erros.Add("Residencia precisa ser selecionada");
            }

            if (erros.HasErrors())
            {
                throw new BusinessException(erros);
            }

            
        }


    }
}
