using HomeControl.Data.Dal.Repository.Base;
using HomeControl.Domain.Dispositivos;
using System.Data.Entity;
using HomeControl.Data.Dal.Repository.Custom.Interfaces;
using HomeControl.Data.Dal.Context;

namespace HomeControl.Data.Dal.Repository.Custom.Implementations
{
    public class DispositivoRepository : AbstractRepository<Dispositivo, int>, IDispositivoDao
    {
        public DispositivoRepository(HomeControlDBContext db) : base(db)
        {

        }
    }
}
