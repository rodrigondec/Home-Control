using HomeControl.Business.Service.Base.Exceptions;
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
        private Residencia obj;

        [TestInitialize]
        public void InitializeTest()
        {
            _residenciaDao = new ResidenciaDao(new EffortHomeControlDatabaseContext().CreateContext());
            _residenciaService = new ResidenciaService(_residenciaDao);
        }

        [TestMethod]
        public void TestAdd()
        {
            obj = new Residencia();
            obj.Nome = "teste";
            int total = _residenciaService.FindAll().Count;
            _residenciaService.Add(obj);
            Assert.AreEqual(total + 1, _residenciaService.FindAll().Count);
        }

        [TestMethod]
        public void TestFind()
        {
            obj = new Residencia();
            obj.Nome = "Teste";
            _residenciaService.Add(obj);
            obj = _residenciaService.Find(1);
            Assert.AreEqual(1, obj.Id);
        }

        [TestMethod]
        public void TestUpdate()
        {
            obj = new Residencia();
            obj.Nome = "Teste";
            _residenciaService.Add(obj);
            obj = _residenciaService.Find(1);
            obj.Nome = "Nome Alterado";
            _residenciaService.Update(obj);
            Assert.AreEqual(obj, _residenciaService.Find(1));
        }


        [TestMethod]
        public void TestValidarNull()
        {
            obj = new Residencia();
            try
            {
                _residenciaService.Validar(obj);
                Assert.Fail("no exception thrown");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }


        [TestMethod]
        public void TestValidarNomeBranco()
        {
            obj = new Residencia();
            obj.Nome = "";
            try
            {
                _residenciaService.Validar(obj);
                Assert.Fail("no exception thrown");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }


    }
}
