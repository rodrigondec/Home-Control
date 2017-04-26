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

namespace HomeControl.Tests.Service
{
    [TestClass]
    public class ComodoServiceTests
    {
        private IComodoService _comodoService;
        private IComodoDao _comodoDao;
        private IResidenciaService _residenciaService;
        private IResidenciaDao _residenciaDao;
        private Residencia objRes;
        private Comodo obj;

        [TestInitialize]
        public void InitializeTest()
        {
            HomeControlDBContext context = new EffortHomeControlDatabaseContext().CreateContext();
            _comodoDao = new ComodoDao(context);
            _residenciaDao = new ResidenciaDao(context);
            _residenciaService = new ResidenciaService(_residenciaDao);
            _comodoService = new ComodoService(_comodoDao, _residenciaService);

            objRes = new Residencia();
            objRes.Nome = "Teste";
            _residenciaService.Add(objRes);
            
        }


        [TestMethod]
        public void TesteComodoAdd()
        {
            obj = new Comodo();
            obj.Nome = "Quarto";
            obj.ResidenciaId = 1;
            int total = _comodoService.FindAll().Count;
            _comodoService.Add(obj);
            Assert.AreEqual(total + 1, _comodoService.FindAll().Count);
        }


        [TestMethod]
        public void TesteComodoFind()
        {
            obj = new Comodo();
            obj.Nome = "Quarto";
            obj.ResidenciaId = 1;
            _comodoService.Add(obj);
            obj = _comodoService.Find(1);
            Assert.AreEqual(1, obj.Id);
        }


        [TestMethod]
        public void TesteComodoUpdateNome()
        {
            obj = new Comodo();
            obj.Nome = "Quarto";
            obj.ResidenciaId = 1;
            _comodoService.Add(obj);
            obj = _comodoService.Find(1);
            obj.Nome = "Nome do Quarto";
            _comodoService.Update(obj);
            Assert.AreEqual(obj, _comodoService.Find(1));
        }

        [TestMethod]
        public void TesteComodoUpdateResidencia()
        {
            objRes = new Residencia();
            objRes.Nome = "Segunda";
            _residenciaService.Add(objRes);

            obj = new Comodo();
            obj.Nome = "Quarto";
            obj.ResidenciaId = 1;
            _comodoService.Add(obj);
            obj = _comodoService.Find(1);
            obj.Nome = "Nome do Quarto";
            obj.ResidenciaId = 2;
            _comodoService.Update(obj);
            Assert.AreEqual(obj, _comodoService.Find(1));
        }


        [TestMethod]
        public void TesteComodoValidarNull()
        {
            obj = new Comodo();
            try
            {
                _comodoService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }


        [TestMethod]
        public void TesteComodoValidarNomeBranco()
        {
            obj = new Comodo();
            obj.Nome = "";
            obj.ResidenciaId = 1;
            try
            {
                _comodoService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }



        [TestMethod]
        public void TesteComodoValidarResidenciaZero()
        {
            obj = new Comodo();
            obj.Nome = "";
            obj.ResidenciaId = 0;
            try
            {
                _comodoService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }

        [TestMethod]
        public void TesteComodoValidarResidenciaErrada()
        {
            obj = new Comodo();
            obj.Nome = "";
            obj.ResidenciaId = 2;
            try
            {
                _comodoService.Validar(obj);
                Assert.Fail("Exceção não lançada");
            }
            catch (Exception ex)
            {
                Assert.IsTrue(ex is BusinessException);
            }
        }

    }
}
