using HomeControl.Dal.Repository.Base;
using HomeControl.Domain.Dispositivos;
using System.Collections.Generic;

namespace HomeControl.Data.Dal.Dao.Custom.Interfaces
{
    public interface IDispositivoDao : IGenericDao<Dispositivo, int>
    {
        List<Dispositivo> FindByPorta(int porta);
    }
}
