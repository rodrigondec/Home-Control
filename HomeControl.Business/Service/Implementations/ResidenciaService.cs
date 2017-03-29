using HomeControl.Business.Service.Base.Exceptions;
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
    /// Serviço cuja finalidade é gerenciar as residências. 
    /// </summary>
    public class ResidenciaService : AbstractService<Residencia, int>
    {
        IResidenciaDao dao = daoFactory.GetResidenciaDao();



        public override Residencia Add(Residencia entity)
        {
            Validar(entity);
            return dao.Add(entity);
        }

        public override Residencia Find(int id)
        {
            return dao.Find(id);
            //throw new NotImplementedException();
        }

        public override List<Residencia> FindAll()
        {
            return dao.FindAll();
        }

        public override Residencia Update(Residencia entity)
        {
            Validar(entity);
            return dao.Update(entity);

        }
        
        public override void Dispose()
        {
            dao.Dispose();
        }

        protected override void Validar(Residencia entity)
        {
            //TODO: Implementar validações
            ErrorList erros = new ErrorList();
            
            if (entity.Nome == null || entity.Nome.Trim() == "")
            {
                erros.Add("<b>Nome Inválido</b>");
            }

            if (erros.HasErrors())
            {
                throw new BusinessException(erros);
            }


            //throw new NotImplementedException();
        }
    }
}
