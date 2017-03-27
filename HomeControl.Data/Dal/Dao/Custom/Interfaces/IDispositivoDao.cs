using HomeControl.Dal.Repository.Base;
using HomeControl.Domain.Dispositivos;

namespace HomeControl.Data.Dal.Dao.Custom.Interfaces
{
    public interface IDispositivoDao<T, ID> : IGenericDao<T, int> where T: Dispositivo
    {
    }
}
