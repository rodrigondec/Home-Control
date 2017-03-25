using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Base.interfaces;
using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Factory;
using HomeControl.Data.Dal.Repository.Custom.Interfaces;
using HomeControl.Domain.Residencia;
using System;
using System.Collections.Generic;

namespace HomeControl.Business.Service.implementation
{
    public class ComodoService : ICrudService<Comodo, int>
    {
        IComodoDao dao = new EntityDaoFactory(new HomeControlDBContext()).getComodoDao();

        public Comodo Add(Comodo entity)
        {
            Validar(entity);
            return dao.Add(entity);
        }

        public void Dispose()
        {
            dao.Dispose();
        }

        public Comodo Find(int id)
        {
            return dao.Find(id);
        }

        public List<Comodo> FindAll()
        {
            return dao.FindAll();
        }

        public Comodo Update(Comodo entity)
        {
            Validar(entity);
            return dao.Update(entity);
        }

        private void Validar(Comodo entity)
        {
            //TODO: Implementar Validações
            List<string> listaErro = new List<string>();

            if (true)
            {
                listaErro.Add("Erro");
            }

            if (listaErro.Count > 0)
            {
                throw new BusinessException(listaErro);
            }
        }
 
    }
}
