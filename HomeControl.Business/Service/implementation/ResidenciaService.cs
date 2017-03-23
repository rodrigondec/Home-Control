using System;
using System.Collections.Generic;
using HomeControl.Business.Service.interfaces;
using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Factory;
using HomeControl.Data.Dal.Repository.Custom.Interfaces;
using HomeControl.Domain.Residencia;
using HomeControl.Business.Service.Base.interfaces;
using HomeControl.Business.Service.Base.Exceptions;

namespace HomeControl.Business.Service.implementation
{
    public class ResidenciaService : ICrudService<Residencia, int>
    {
        IResidenciaDao dao = new EntityDaoFactory(new HomeControlDBContext()).getResidenciaDao();

        Residencia ICrudService<Residencia, int>.Add(Residencia entity)
        {
            Validar(entity);
            return dao.Add(entity);

        }

        Residencia ICrudService<Residencia, int>.Find(int id)
        {
            return dao.Find(id);
            //throw new NotImplementedException();
        }

        List<Residencia> ICrudService<Residencia, int>.FindAll()
        {
            return dao.FindAll();
        }

        Residencia ICrudService<Residencia, int>.Update(Residencia entity)
        {
            Validar(entity);
            return dao.Update(entity);

        }

        private void Validar(Residencia entity)
        {
            List<string> listaErro = new List<string>();

            if (true)
            {
                listaErro.Add("Erro");
            }

            if(listaErro.Count > 0)
            {
                throw new BusinessException(listaErro);
            }
        }

        void IDisposable.Dispose()
        {
            dao.Dispose();
        }



    }
}
