using HomeControl.Data.Dal.Dao.Base;
using HomeControl.Domain.Dispositivos;
using System.Data.Entity;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Data.Dal.Context;

namespace HomeControl.Data.Dal.Dao.Custom.Implementations
{
    public class ControladorDao : AbstractDao<Controlador, int>, IControladorDao
    {
        public ControladorDao(HomeControlDBContext db) : base(db)
        {
        }
    }
}
