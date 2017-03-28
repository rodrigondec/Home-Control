using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Dao.Base;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Sensores;

namespace HomeControl.Data.Dal.Dao.Custom.Implementations
{
    public class SensorDao : AbstractDao<Sensor, int>, ISensorDao
    {
        public SensorDao(HomeControlDBContext db) : base(db)
        {

        }
    }
}