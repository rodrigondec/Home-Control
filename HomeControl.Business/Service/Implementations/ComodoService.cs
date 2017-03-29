﻿using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Base.interfaces;
using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Factory;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Residencia;
using System;
using System.Collections.Generic;

namespace HomeControl.Business.Service.Implementations
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

        protected override void Validar(Comodo entity)
        {
            ErrorList erros = new ErrorList();

            if (true)
            {
                erros.Add("Erro");
            }

            if (erros.HasErrors())
            {
                throw new BusinessException(erros);
            }

            
        }


    }
}
