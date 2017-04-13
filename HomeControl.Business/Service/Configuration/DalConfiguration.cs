using HomeControl.Data.Dal.Exceptions;
using HomeControl.Data.Dal.Factory;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Utils.Xml;

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
            String factory = XmlReader.GetAppSettingUsingConfigurationManager("DalFactory");

            switch (factory)
            {
                case "Entity":
                    return new EntityDaoFactory(new Data.Dal.Context.HomeControlDBContext());
                case "AdoNet":
                    return new AdoNetRepositoryFactory();
                default:
                    throw new DalException("Erro na configuração do acesso à dados ");
            }

        }
    }
}
