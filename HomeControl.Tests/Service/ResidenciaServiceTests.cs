using HomeControl.Business.Service.Implementations;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Residencia;
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
        private IResidenciaService _residenciaService;
        private IResidenciaDao _residenciaDao;

        [TestInitialize]
        public void InitializeTest()
        {
            _residenciaDao = new ResidenciaDao(new EffortHomeControlDatabaseContext().CreateContext());
            _residenciaService = new ResidenciaService(_residenciaDao);
        }

        [TestMethod]
        public void TestAdd()
        {
            Residencia r = new  Residencia();
            r.Nome = "teste";
            int total = _residenciaService.FindAll().Count;
            _residenciaService.Add(r);
            Assert.AreEqual(_residenciaService.FindAll().Count, total+1);
        }

        //[TestMethod]
        //public void Test


    }
}
