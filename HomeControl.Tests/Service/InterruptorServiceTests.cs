using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Tests.Dal;
using HomeControl.Business.Service.Implementations;
using HomeControl.Domain.Residencia;
using HomeControl.Data.Dal.Context;
using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Domain.Dispositivos;
using HomeControl.Domain.Interruptores;

namespace HomeControl.Tests.Service
{
    [TestClass]
    public class InterruptorServiceTests
    {
        private IInterruptorDao _interruptorDao;
        private IComodoDao _comodoDao;
        private IComodoService _comodoService;
        private IEmbarcadoService _embarcadoService;
        private IInterruptorService _interruptorService;
        private IResidenciaService _residenciaService;
        private IResidenciaDao _residenciaDao;
        private IEmbarcadoDao _embarcadoDao;
        private IDispositivoDao _dispositivoDao;
        private DefaultDispositivoService _dftDispositivo;

        private Interruptor obj;
        private Residencia objRes;
        private Comodo objCom;
        private Embarcado objEmb;

        [TestInitialize]
        public void InitializeTest()
        {
            HomeControlDBContext context = new EffortHomeControlDatabaseContext().CreateContext();
            _interruptorDao = new InterruptorDao(context);
            _residenciaDao = new ResidenciaDao(context);
            _embarcadoDao = new EmbarcadoDao(context);
            _comodoDao = new ComodoDao(context);
            _dispositivoDao = new DispositivoDao(context);

            _dftDispositivo = new DefaultDispositivoService(_dispositivoDao);
            _residenciaService = new ResidenciaService(_residenciaDao);
            _comodoService = new ComodoService(_comodoDao, _residenciaService);
            _embarcadoService = new EmbarcadoService(_embarcadoDao);
            _interruptorService = new InterruptorService(_interruptorDao, _comodoService, _embarcadoService, _dftDispositivo);

            objRes = new Residencia();
            objRes.Nome = "Teste";
            _residenciaService.Add(objRes);

            objCom = new Comodo();
            objCom.Nome = "Quarto Teste";
            objCom.ResidenciaId = 1;
            _comodoService.Add(objCom);

            objEmb = new Embarcado();
            objEmb.MacAddress = "Mac";
            objEmb.Socket = "192.168.1.1:10";
            objEmb.Nome = "Raspeberry";
            _embarcadoService.Add(objEmb);

        }

        [TestMethod]
        public void TestInterruptorAdd()
        {
            obj = new Interruptor();
            obj.Embarcadoid = 1;
            obj.ComodoId = 1;
            obj.Porta = 10;

            int total = _interruptorService.FindAll().Count;
            _interruptorService.Add(obj);
            Assert.AreEqual(total + 1, _interruptorService.FindAll().Count);
        }


        [TestMethod]
        public void TestInterruptorFind()
        {
            obj = new Interruptor();
            obj.Embarcadoid = 1;
            obj.ComodoId = 1;
            obj.Porta = 10;

            _interruptorService.Add(obj);
            obj = _interruptorService.Find(1);
            Assert.AreEqual(1, obj.Id);
        }


        [TestMethod]
        public void TestEmbarcadoUpdatePorta()
        {
            obj = new Interruptor();
            obj.Embarcadoid = 1;
            obj.ComodoId = 1;
            obj.Porta = 10;

            _interruptorService.Add(obj);
            obj = null;
            obj = _interruptorService.Find(1);
            obj.Porta = 15;
            _interruptorService.Update(obj);
            Assert.AreEqual(obj, _interruptorService.Find(1));
        }


        [TestMethod]
        public void TestEmbarcadoValidarNull()
        {
            obj = new Interruptor();
         

            try
            {
                _interruptorService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }

        [TestMethod]
        public void TestEmbarcadoValidarEmbarcadoNull()
        {
            obj = new Interruptor();
            obj.ComodoId = 1;
            obj.Porta = 10;

            try
            {
                _interruptorService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }


        [TestMethod]
        public void TestEmbarcadoValidarComodoNull()
        {
            obj = new Interruptor();
            obj.Embarcadoid = 1;
            obj.Porta = 10;

            try
            {
                _interruptorService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }


        [TestMethod]
        public void TestEmbarcadoValidarPortaZero()
        {
            obj = new Interruptor();
            obj.Embarcadoid = 1;
            obj.ComodoId = 1;
            obj.Porta = 0;

            try
            {
                _interruptorService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }


        [TestMethod]
        public void TestEmbarcadoValidarPortaRepetida()
        {
            obj = new Interruptor();
            obj.Embarcadoid = 1;
            obj.ComodoId = 1;
            obj.Porta = 10;
            _interruptorService.Add(obj);

            try
            {
                _interruptorService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }
    }
}
