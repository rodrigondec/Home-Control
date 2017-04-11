using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Base.interfaces;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Sensores;
using System;
using System.Collections.Generic;

namespace HomeControl.Business.Service.Implementations
{
    public class SensorService : AbstractService<Sensor, int>, ISensorService
    {
        private ISensorDao dao;

        public SensorService()
        {
            dao = DaoFactory.GetSensorDao();
            this.GenericDao = dao;
        }

        public override Sensor Add(Sensor entity)
        {
            Validar(entity);
            return dao.Add(entity);
        }

        public override void Dispose()
        {
            dao.Dispose();
        }

        public override Sensor Find(int id)
        {
            return dao.Find(id);
        }

        public override List<Sensor> FindAll()
        {
            return dao.FindAll();
        }

        public override Sensor Update(Sensor entity)
        {
            Validar(entity);
            return dao.Update(entity);
        }

        protected override void Validar(Sensor entity)
        {
            ErrorList erros = new ErrorList();

            if (entity == null)
            {
                erros.Add("Sensor precisa ser preenchido");
            }

            if(entity.Comodo == null)
            {
                erros.Add("Sensor precisar estar associado a um Cômodo");
            }
            
            if (erros.HasErrors())
            {
                throw new BusinessException(erros);
            }
        }
    }
}
