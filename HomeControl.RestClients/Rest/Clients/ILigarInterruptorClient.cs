using HomeControl.Domain.Dispositivos;
using HomeControl.Domain.Interruptores;

namespace Rest.Clients
{
    public interface ILigarInterruptorClient
    {
        void LigarDispositivo(Interruptor dispositivo);
        void DesligarDispositivo(Interruptor dispositivo);
        bool GetStatusInterruptor(Interruptor interruptor);
    }
}