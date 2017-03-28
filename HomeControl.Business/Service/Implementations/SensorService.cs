using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Base.interfaces;
using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Sensores;
using System;
using System.Collections.Generic;

namespace HomeControl.Business.Service.Implementations
{
    class SensorService : AbstractService<Sensor, int>
    {
        private ISensorDao dao;

        public SensorService()
        {
            dao = daoFactory.GetSensorDao();
        }

        public override Sensor Add(Sensor entity)
        {
            Validar(entity);
            return dao.Add(entity);
        }

        public override void Dispose()
        {
            dao.Dispose()
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
            //to do: Validações
            throw new NotImplementedException();
        }
    }
}
