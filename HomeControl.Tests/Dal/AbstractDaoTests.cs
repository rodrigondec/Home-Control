using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Dao.Base;
using HomeControl.Domain;
using HomeControl.Domain.Residencia;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Moq;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Tests.Dal
{
    [TestClass]
    public class AbstractDaoTests
    {

        public IHomeControlDBContext _testDbContext;
        public EffortHomeControlDatabaseContext _effortDbContextProvider;

        [TestInitialize]
        public void InitializeTests()
        {
            _effortDbContextProvider = new EffortHomeControlDatabaseContext();
            _testDbContext = _effortDbContextProvider.CreateContext();
            //PopularDados
        }

        [TestMethod]
        public void TestFindAll()
        {
        }

        [TestMethod]
        public void TestFind()
        {

        }

        [TestMethod]
        public void TestUpdate()
        {
        //    AbstractDao<Residencia, int> dao = new DefaultDao<Residencia, int>((DbContext)_testDbContext);
        //    Residencia residencia = new Residencia() { Id = 0, Nome = "Minha casa" };
        //    dao.Add(residencia);


        //    Assert.AreEqual(_testDbContext.Residencias.Count(), 1);
        //    Assert.AreNotEqual(residencia.Id, 0);
        }

        [TestMethod]
        public void TestTestAdd()
        {
            AbstractDao<Residencia, int> dao = new DefaultDao<Residencia, int>((DbContext)_testDbContext);
            Residencia residencia = new Residencia() { Id = 0, Nome = "Minha casa" };
            dao.Add(residencia);
            Assert.AreEqual(_testDbContext.Residencias.Count(), 1);
            Assert.AreNotEqual(residencia.Id, 0);
        }

        [TestMethod]
        public void TestRemove()
        {
            AbstractDao<Residencia, int> dao = new DefaultDao<Residencia, int>((DbContext)_testDbContext);
            int quantidadeAntesAddRemover = _testDbContext.Residencias.Count();

            Residencia residencia = new Residencia() { Id = 0, Nome = "Minha casa" };
            dao.Add(residencia);
            dao.Remove(residencia);

            Assert.AreEqual(_testDbContext.Residencias.Count(), quantidadeAntesAddRemover);
        }

    }
}
