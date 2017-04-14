using HomeControl.Data.Dal.Context;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Tests.Dal
{
    public class EffortHomeControlDatabaseContext : ConnectionProviderTest
    {

        public IHomeControlDBContext CreateContext()
        {
            base.CreateConnection();
            var context = new HomeControlDBContext(_connection);

            return context;
        }

        public void Dispose(IHomeControlDBContext context)
        {
            if (context != null)
            {
                context.Dispose();
            }
        }   

    }
}
