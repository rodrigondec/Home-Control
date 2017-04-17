using HomeControl.Domain.Dispositivos;

namespace Operation.Comandos.Interruptores
{
    public interface ILigarInterruptorClient
    {
        void LigarDispositivo(Dispositivo dispositivo);
        void DesligarDispositivo(Dispositivo dispositivo);
    }
}