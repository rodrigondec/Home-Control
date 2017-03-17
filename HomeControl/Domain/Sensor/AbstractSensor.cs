using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace HomeControl.Domain.Sensor
{
    public abstract class AbstractSensor : Dispositivo, Sensor
    {
        public float valorAtual;
        public abstract float getValorAtual();
    }
}