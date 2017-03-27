using HomeControl.Data.Dal.Exceptions;
using HomeControl.Data.Dal.Factory;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Configuration
{
    public class DalConfiguration
    {
        private static DaoFactory instance;

        public static DaoFactory GetDaoFactory()
        {
            if (instance == null)
            {
                instance = CreateFactory();
            }

            return instance;

        }

        private static DaoFactory CreateFactory()
        {
            String factory = "1";

            switch (factory)
            {
                case "1":
                    return new EntityDaoFactory(new Data.Dal.Context.HomeControlDBContext());
                case "2":
                    return new AdoNetRepositoryFactory();
                default:
                    throw new DalException("Erro na configuração do acesso à dados ");
            }

        }
    }
}
