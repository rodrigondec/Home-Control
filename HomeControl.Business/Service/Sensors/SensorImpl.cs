using HomeControl.Domain.Sensores;
using Rest.Clients;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Sensors
{
    public class SensorImpl : ISensor
    {
        public Sensor Sensor { get; set; }

        public SensorImpl(Sensor sensor)
        {
            Sensor = sensor;
        }

        public float GetValorAtual()
        {
            SensorClient client = SensorClient.Instance;
            return (float) client.RecuperarValorAtual(Sensor);
        }
    }
}
