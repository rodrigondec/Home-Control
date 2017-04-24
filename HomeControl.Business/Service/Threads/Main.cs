using HomeControl.Business.Service.Interfaces;
using HomeControl.Business.Service.Monitor;
using HomeControl.Domain.Dispositivos;
using HomeControl.Domain.Interruptores;
using HomeControl.Domain.Residencia;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Threads
{
    public class Main
    {
        private bool _shouldStop = false;
        private IInterruptorService _interruptorService;
        private IPotenciometroService _potenciometroService;
        private SensorMonitor _sensorMonitor;

        public Residencia Residencia { get; set; }
        public Comodo Comodo { get; set; }        

        public void Run()
        {
            while (_shouldStop)
            {

                verificaSeExisteAlguemNaResidencia(Residencia);

                foreach (Comodo comodo in Residencia.Comodos)
                {

                    VerificaSeTemAlguemNoComodo(comodo);
                    VerificaSeATemperaturaEstaAgradavel(comodo);                    

                }
                
            }

        }

        private void VerificaSeATemperaturaEstaAgradavel(Comodo comodo)
        {
            throw new NotImplementedException();
        }

        private void verificaSeExisteAlguemNaResidencia(Residencia residencia)
        {
            bool existeAlguemPresente = false;

            //Desligar todos os Knobs e interruptores
            if (!existeAlguemPresente)
            {
                List<Interruptor> interruptores = _interruptorService.FindAll();
            }

        }

        private List<Dispositivo> GetAllDispositivosResidencia(Residencia residencia)
        {
            //GetAllDispositivosResidencia();
            throw new NotImplementedException();
        }

        private void VerificaSeTemAlguemNoComodo(Comodo comodo)
        {            

            if(_sensorMonitor.HasPessoasPresentes(comodo)){

            }
            else
            {

            }

        }

        private void VerificaSeExisteAlguemNaResidencia(Residencia residencia)
        {
            //GetAllSensoresPresencaResidencia()
            throw new NotImplementedException();
        }

        private void Stop()
        {
            _shouldStop = true;
        }

    }
}
