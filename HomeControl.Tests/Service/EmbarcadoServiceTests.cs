using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Implementations;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Dispositivos;
using HomeControl.Tests.Dal;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;

namespace HomeControl.Tests.Service
{
    [TestClass]
    public class EmbarcadoServiceTests
    {
        private IEmbarcadoDao _embarcadoDao;
        private IEmbarcadoService _embarcadoService;
        private Embarcado obj;

        [TestInitialize]
        public void InitializeTest()
        {
            HomeControlDBContext context = new EffortHomeControlDatabaseContext().CreateContext();
            _embarcadoDao = new EmbarcadoDao(context);
            _embarcadoService = new EmbarcadoService(_embarcadoDao);
        }

        [TestMethod]
        public void TestEmbarcadoAdd()
        {
            obj = new Embarcado();
            obj.MacAddress = "Mac";
            obj.Socket = "192.168.1.1:10";
            obj.Nome = "Raspeberry";
            int total = _embarcadoService.FindAll().Count;
            _embarcadoService.Add(obj);
            Assert.AreEqual(total + 1, _embarcadoService.FindAll().Count);
        }


        [TestMethod]
        public void TestEmbarcadoFind()
        {
            obj = new Embarcado();
            obj.MacAddress = "Mac";
            obj.Socket = "192.168.1.1:10";
            obj.Nome = "Raspeberry";
            _embarcadoService.Add(obj);
            obj = _embarcadoService.Find(1);
            Assert.AreEqual(1, obj.Id);
        }


        [TestMethod]
        public void TestEmbarcadoUpdateNome()
        {
            obj = new Embarcado();
            obj.MacAddress = "Mac";
            obj.Socket = "192.168.1.1:10";
            obj.Nome = "Raspeberry";
            _embarcadoService.Add(obj);
            obj = _embarcadoService.Find(1);
            obj.Nome = "Raspeberrry 2";
            _embarcadoService.Update(obj);
            Assert.AreEqual(obj, _embarcadoService.Find(1));
        }


        [TestMethod]
        public void TestEmbarcadoValidarNull()
        {
            obj = new Embarcado();
            try
            {
                _embarcadoService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }

        [TestMethod]
        public void TestEmbarcadoValidarNome()
        {
            obj = new Embarcado();
            obj.Nome = "";
            obj.MacAddress = "Mac";
            obj.Socket = "192.168.1.1:10";
            try
            {
                _embarcadoService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }


        [TestMethod]
        public void TestEmbarcadoValidarMac()
        {
            obj = new Embarcado();
            obj.Nome = "Raspeberry";
            obj.MacAddress = "";
            obj.Socket = "192.168.1.1:10";
            try
            {
                _embarcadoService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }


        [TestMethod]
        public void TestEmbarcadoValidarSocket()
        {
            obj = new Embarcado();
            obj.Nome = "Raspeberry";
            obj.MacAddress = "Mac";
            obj.Socket = "";
            try
            {
                _embarcadoService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }
    }
}
