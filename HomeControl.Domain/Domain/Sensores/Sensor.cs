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

        public override void activate()
        {
            throw new NotImplementedException();
        }

        public override void deactivate()
        {
            throw new NotImplementedException();
        }

        public float getValorAtual()
        {
            throw new NotImplementedException();
        }

        //public abstract float getValorAtual();

        public override bool isActive()
        {
            throw new NotImplementedException();
        }
    }
}