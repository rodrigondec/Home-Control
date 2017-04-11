using HomeControl.Data.Dal.Dao.Base;
using HomeControl.Domain.Domain.Log;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.Entity;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;

namespace HomeControl.Data.Dal.Dao.Custom.Implementations
{
    public class HistoricoUsoDao : AbstractDao<HistoricoUsoDispositivo, int>,IHistoricoUsoDispositivoDao
    {
        public HistoricoUsoDao(DbContext db) : base(db)
        {
        }
    }
}
