using HomeControl.Data.Dal.Repository.Base;
using HomeControl.Domain.Dispositivos;
using System.Data.Entity;
using HomeControl.Data.Dal.Repository.Custom.Interfaces;

namespace HomeControl.Data.Dal.Repository.Custom.Implementations
{
    public class ControladorRepository : AbstractRepository<Controlador, int>, IControladorRepository
    {
        public ControladorRepository(DbContext db) : base(db)
        {
        }
    }
}
