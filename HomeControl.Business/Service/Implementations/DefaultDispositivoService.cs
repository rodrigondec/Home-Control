using HomeControl.Data.Dal.Dao.Custom.Implementations;
using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Dispositivos;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Implementations
{
    public class DefaultDispositivoService : AbstractService<Dispositivo, int>
    {

        private IDispositivoDao _dispositivoDao;

        public DefaultDispositivoService(IDispositivoDao dispositivoDao) : base(dispositivoDao)
        {
            _dispositivoDao = dispositivoDao;
        }

        public List<Dispositivo> FindByPorta(int porta)
        {
            return _dispositivoDao.FindByPorta(porta);
            
        }

        public DefaultDispositivoService() : this(DaoFactory.GetDispositivoDao()) { }

        public override void Validar(Dispositivo entity)
        {

        }
    }
}
