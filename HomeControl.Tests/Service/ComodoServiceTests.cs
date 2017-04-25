using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;

namespace HomeControl.Tests.Service
{
    [TestClass]
    public class ComodoServiceTests
    {
        private IComodoService _comodoService;
        private IComodoDao _comodoDao;
        private IResidenciaService _residenciaService;

        [TestInitialize]
        public void InitializeTest()
        {
      
            //_residenciaDao = new ResidenciaDao(new EffortHomeControlDatabaseContext().CreateContext());
        }


        [TestMethod]
        public void TestMethod1()
        {
        }
    }
}
