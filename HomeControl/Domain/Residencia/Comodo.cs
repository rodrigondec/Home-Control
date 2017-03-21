using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace HomeControl.Domain.Residencia
{
    public class Comodo
    {
        [Key]
        private int IdComodo { get; set; }
        private string Nome { get; set; }
        private Residencia Residencia { get; set; }
    }
}