using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Data.Dal.Exceptions
{
    public class DalException : Exception
    {
        public DalException(String error) : base(error) { }

    }
}
