using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Base.Exceptions
{
    public class ErrorList
    {
        public ErrorList()
        {
            this.ErrorCodes = new List<String>();
        }

        public List<String> ErrorCodes { get; set; }

        public Boolean HasErrors()
        {
            return ErrorCodes.Count != 0;
        }
        public void Add(String error)
        {
            this.ErrorCodes.Add(error);
        }

        public void Remove(String error)
        {
            this.ErrorCodes.Remove(error);
        }

    }

}
