using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Base.interfaces;
using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Factory;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Residencia;
using System;
using System.Collections.Generic;

namespace HomeControl.Business.Service.Implementation
{
    /// <summary>
    /// Serviço cuja finalidade é gerenciar os comodos de uma residência. 
    /// </summary>
    public class ComodoService : AbstractService<Comodo, int>
    {
        private IComodoDao dao;

        public ComodoService()
        {
            dao = daoFactory.GetComodoDao();
        }

        public override Comodo Add(Comodo entity)
        {
            Validar(entity);

            return dao.Add(entity);
        }

        public override void Dispose()
        {
            dao.Dispose();
        }

        public override Comodo Find(int id)
        {
            return dao.Find(id);
        }

        public override List<Comodo> FindAll()
        {
            return dao.FindAll();
        }

        public override Comodo Update(Comodo entity)
        {
            Validar(entity);
            return dao.Update(entity);
        }

        /// <summary>
        /// Efetua a validação de um comodo. Caso o comodo fuja 
        /// das regras de validação, o método pode lançar 'Business Exception'.
        /// </summary>
        /// <param name="entity"></param>
        /// <exception cref="BusinessException"></exception>
        /// <returns></returns>
        private ErrorList Validar(Comodo entity)
        {
            //TODO: Implementar Validações
            ErrorList erros = new ErrorList();

            if (true)
            {
                erros.Add("Erro");
            }

            if (erros.HasErrors())
            {
                throw new BusinessException(erros);
            }

            return erros;

        }

    }
}
