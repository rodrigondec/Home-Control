using HomeControl.Data.Dal.Repository.Base;
using HomeControl.Domain.Dispositivos;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.Entity;
using HomeControl.Data.Dal.Repository.Interfaces;

namespace HomeControl.Data.Dal.Repository.Implementations
{
    public class ControladorRepository : AbstractRepository<Controlador, int>, IControladorRepository
    {
        public ControladorRepository(DbContext db) : base(db)
        {
        }
    }
}
