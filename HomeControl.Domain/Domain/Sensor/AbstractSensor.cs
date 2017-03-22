using HomeControl.Domain.Dispositivos;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace HomeControl.Domain.Sensor
{
    public abstract class AbstractSensor : Dispositivo, Sensor
    {
        [NotMapped]
        public float valorAtual;
        public abstract float getValorAtual();
    }
}