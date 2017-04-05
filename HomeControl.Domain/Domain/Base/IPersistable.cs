using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Domain.Domain.Base
{
    public interface IPersistable<ID>
    {
        ID Id { get; set; }
    }
}
