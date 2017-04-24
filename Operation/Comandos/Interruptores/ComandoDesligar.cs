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
    public class ComandoDesligar : ComandoAbstrato<Interruptor>
    {
        private ILigarInterruptorClient _client;

        public ComandoDesligar(ILigarInterruptorClient client)
        {
            _client = client;
        }

        public override void Execute()
        {
            _client.DesligarDispositivo(Dispositivo);
        }

        public override void UnExecute()
        {
            _client.LigarDispositivo(Dispositivo);
        }
    }
}
