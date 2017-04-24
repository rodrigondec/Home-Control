using HomeControl.Domain.Residencia;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Monitor
{
    public class SensorMonitor
    {

        public double getTemperaturaComodo(Comodo comodo)
        {
            return 30.0;
        }

        public Boolean HasPessoasPresentes(Comodo comodo)
        {
            return true;
        }

    }
}
