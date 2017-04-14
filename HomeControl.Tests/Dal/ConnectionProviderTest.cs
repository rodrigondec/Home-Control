using Effort;
using System;
using System.Collections.Generic;
using System.Data.Common;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Tests.Dal
{
    public class ConnectionProviderTest : IDisposable
    {
        protected DbConnection _connection;

        protected void CreateConnection()
        {
            if (_connection == null)
            {
                _connection = DbConnectionFactory.CreateTransient();
            }
        }

        public void Dispose()
        {
            throw new NotImplementedException();
        }
    }
}
