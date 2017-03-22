using HomeControl.Data.Dal.Repository.Base;
using HomeControl.Data.Dal.Repository.Interfaces;
using HomeControl.Domain.Residencia;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.Entity;

namespace HomeControl.Data.Dal.Repository.Implementations
{
    public class ResidenciaRepository : AbstractRepository<Residencia, int>, IResidenciaRepository
    {
        public ResidenciaRepository(DbContext db) : base(db)
        {

        }

    }
}
