using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Base.Exceptions
{
    public class BusinessException : Exception
    {
        List<string> ListaMensagem;

        public BusinessException(string messagem) : base(messagem) { }

        public BusinessException(List<string> Lista) : base() {
            this.ListaMensagem = Lista;
        }

    }
}
