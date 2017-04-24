using HomeControl.Domain.Interruptores;
using Rest.Clients;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Interruptores
{
    public class InterruptorImpl : IInterruptor
    {
        public Interruptor Interruptor { get; set; }

        private ILigarInterruptorClient _client;

        public InterruptorImpl(Interruptor interruptor)
        {
            Interruptor = interruptor;
            _client = new LigarInterruptorClient();
        }

        public void DesligarDispositivo()
        {
            _client.LigarDispositivo(Interruptor);
        }

        public bool GetStatus()
        {
            return _client.GetStatusInterruptor(Interruptor);
        }

        public void LigarDispositivo()
        {
            _client.LigarDispositivo(Interruptor);
        }
    }
}
