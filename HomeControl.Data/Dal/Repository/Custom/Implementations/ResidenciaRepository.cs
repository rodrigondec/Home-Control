using HomeControl.Data.Dal.Repository.Base;
using HomeControl.Domain.Residencia;
using System.Data.Entity;
using HomeControl.Data.Dal.Repository.Custom.Interfaces;

namespace HomeControl.Data.Dal.Repository.Custom.Implementations
{
    public class ResidenciaRepository : AbstractRepository<Residencia, int>, IResidenciaRepository
    {
        public ResidenciaRepository(DbContext db) : base(db)
        {

        }

    }
}
