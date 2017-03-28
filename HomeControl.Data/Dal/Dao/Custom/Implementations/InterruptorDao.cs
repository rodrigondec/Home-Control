using HomeControl.Data.Dal.Context;
using HomeControl.Data.Dal.Dao.Base;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Interruptores;

namespace HomeControl.Data.Dal.Dao.Custom.Implementations
{
    public class InterruptorDao : AbstractDao<Interruptor, int>, IInterruptorDao
    {
        public InterruptorDao(HomeControlDBContext db) : base(db)
        {

        }
    }
}
