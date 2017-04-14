using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Base.interfaces;
using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Factory;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Residencia;
using System;
using System.Collections.Generic;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Dal.Repository.Base;

namespace HomeControl.Business.Service.Implementations
{
    /// <summary>
    /// Serviço cuja finalidade é gerenciar as residências. 
    /// </summary>
    public class ResidenciaService : AbstractService<Residencia, int>, IResidenciaService
    {
        public IResidenciaDao Dao { get; set; }

        public ResidenciaService(IResidenciaDao dao) : base(dao)
        {
            this.Dao = dao;
        }

        public ResidenciaService()
        {
            Dao = DaoFactory.GetResidenciaDao();
            base.GenericDao = Dao;
        }

        public override Residencia Add(Residencia entity)
        {
            if (entity.Id > 0)
            {
                throw new BusinessException("Residencia já existente.");
            }

            Validar(entity);
            return Dao.Add(entity);
        }

        public override Residencia Find(int id)
        {
            return Dao.Find(id);
        }

        public override List<Residencia> FindAll()
        {
            return Dao.FindAll();
        }

        public override Residencia Update(Residencia entity)
        {
            if (entity.Id <= 0)
            {
                throw new BusinessException("Residencia não existente.");
            }
            Validar(entity);
            return Dao.Update(entity);

        }

        public override void Dispose()
        {
            base.Dispose();
            Dao.Dispose();
        }

        public override void Validar(Residencia entity)
        {
            //TODO: Implementar validações
            ErrorList erros = new ErrorList();

            if (entity.Nome == null || entity.Nome.Trim() == "")
            {
                erros.Add("Nome Inválido.");
            }

            if (erros.HasErrors())
            {
                throw new BusinessException(erros);
            }

        }
    }
}
