using HomeControl.Data.Dal.Repository.Base;
using HomeControl.Data.Dal.Repository.Interfaces;
using HomeControl.Domain.Dispositivos;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.Entity;

namespace HomeControl.Data.Dal.Repository.Implementations
{
    public class DispositivoRepository : AbstractRepository<Dispositivo, int>, IDispositivoRepository
    {
        public DispositivoRepository(DbContext db) : base(db)
        {

        }
    }
}
