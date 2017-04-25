using HomeControl.Domain.Dispositivos;
using HomeControl.Domain.Sensores;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Rest.Clients;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Tests.Rest
{
    [TestClass]
    public class SensorClientTest
    {
        [TestMethod]
        public void ValorSensorTestMethod()
        {
            Sensor sensor = new Sensor();
            sensor.Porta = 1;
            sensor.Embarcado = new Embarcado()
            {
                Socket = "127.0.0.1:8080"
            };

            SensorClient sensorClient = SensorClient.Instance;

            double valorAtual = sensorClient.RecuperarValorAtual(sensor);

            Assert.AreEqual(valorAtual, 35.0);

        }

    }
}
