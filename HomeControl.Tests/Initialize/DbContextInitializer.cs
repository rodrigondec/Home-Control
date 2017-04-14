using Effort.Provider;
using HomeControl.Data.Dal.Context;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Tests.Initialize
{
    [TestClass]
    public class DbContextInitializer
    {

        [AssemblyInitialize]
        public static void AssemblyInit(TestContext context)
        {
            EffortProviderConfiguration.RegisterProvider();
        }
    }
}
