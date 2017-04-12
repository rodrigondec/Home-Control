using HomeControl.Domain.Dispositivos;
using HomeControl.Domain.Domain.Security;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Domain.Domain.Log
{
    public class HistoricoUsoDispositivo : IPersistable<int>
    {

        [Key]
        public int Id { get; set;  }
        public virtual Usuario Usuario { get; set; }
        public virtual Dispositivo Dispositivo { get; set; }

    }
}
