using HomeControl.Domain.Interruptores;
using Operation.Comandos.Base;
using Rest.Clients;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Operation.Comandos.Interruptores
{
    public class ComandoLigar : ComandoAbstrato<Interruptor>
    {
        private ILigarInterruptorClient _ligarDispositivoClient;
     
        public ComandoLigar(ILigarInterruptorClient client)
        {
            _ligarDispositivoClient = client;         
        }

        public override void Execute()
        {
            _ligarDispositivoClient.LigarDispositivo(Dispositivo);
        }

        public override void UnExecute()
        {
            _ligarDispositivoClient.DesligarDispositivo(Dispositivo);
        }
    }
}
