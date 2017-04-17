using HomeControl.Domain.Sensores;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Operation.Comandos.Sensores.Clients
{
    interface SensorClient
    {
        void RecuperarValorAtual(Sensor sensor);
    }
}
