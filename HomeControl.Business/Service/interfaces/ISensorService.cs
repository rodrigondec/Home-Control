using HomeControl.Business.Service.Base.interfaces;
using HomeControl.Domain.Sensores;

namespace HomeControl.Business.Service.Interfaces
{
    public interface ISensorService : ICrudService<Sensor, int>
    {
        float GetValorAtual(Sensor sensor);
    }
}
