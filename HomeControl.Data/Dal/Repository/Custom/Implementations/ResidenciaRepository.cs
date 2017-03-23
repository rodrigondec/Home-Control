using HomeControl.Data.Dal.Repository.Base;
using HomeControl.Domain.Residencia;
using System.Data.Entity;
using HomeControl.Data.Dal.Repository.Custom.Interfaces;
using HomeControl.Data.Dal.Context;

namespace HomeControl.Data.Dal.Repository.Custom.Implementations
{
    public class ResidenciaRepository : AbstractRepository<Residencia, int>, IResidenciaDao
    {
        public ResidenciaRepository(HomeControlDBContext db) : base(db)
        {

        }

    }
}
