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

        public override void Activate()
        {
            throw new NotImplementedException();
        }

        public override void Deactivate()
        {
            throw new NotImplementedException();
        }

        public float GetValorAtual()
        {
            throw new NotImplementedException();
        }      

        public override bool IsActive()
        {
            throw new NotImplementedException();
        }
    }
}