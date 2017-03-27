using HomeControl.Data.Dal.Dao.Base;
using HomeControl.Domain.Residencia;
using System.Data.Entity;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Data.Dal.Context;

namespace HomeControl.Data.Dal.Dao.Custom.Implementations
{
    public class ResidenciaDao : AbstractDao<Residencia, int>, IResidenciaDao
    {
        public ResidenciaDao(HomeControlDBContext db) : base(db)
        {

        }

    }
}
