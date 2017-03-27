using HomeControl.Domain.Dispositivos;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace HomeControl.Domain.Sensores
{
    public class Sensor : Dispositivo, ISensor
    {
        [NotMapped]
        public float valorAtual;
        public abstract float getValorAtual();
    }
}