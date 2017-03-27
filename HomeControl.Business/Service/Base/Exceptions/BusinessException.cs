using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Base.Exceptions
{
    public class BusinessException : Exception
    {
        public ErrorList Errors { get; set; }

        public BusinessException(string messagem) : base(messagem) { }

        public BusinessException(ErrorList lista) : base() {
            this.Errors = lista;
        }

    }
}
