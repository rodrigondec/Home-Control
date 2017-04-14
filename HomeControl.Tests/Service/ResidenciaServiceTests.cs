using HomeControl.Business.Service.Interfaces;
using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Tests.Dal;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Tests.Service
{
    [TestClass]
    public class ResidenciaServiceTests
    {
        private IResidenciaService  _residenciaService;
        private IResidenciaDao _residenciaDao;

        [TestInitialize]
        public void InitializeTest()
        {           
            //_residenciaDao = new ResidenciaDao(new EffortHomeControlDatabaseContext().CreateContext());
        }

        [TestMethod]
        public void TestAdd()
        {

        }



    }
}
