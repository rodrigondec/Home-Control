using HomeControl.Domain.Sensores;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Rest.Clients
{
    public interface ISensorClient
    {
        double RecuperarValorAtual(Sensor sensor);
    } 
}
