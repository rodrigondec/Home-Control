using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using HomeControl.Domain.Domain.Log;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Implementations
{
    public class HistoricoUsoDispositivoService : AbstractService<HistoricoUsoDispositivo, int>, IHistoricoUsoDispositivoService
    {
        public IHistoricoUsoDispositivoDao Dao { get; set; }

        public HistoricoUsoDispositivoService()
        {
            this.Dao = DaoFactory.GetHistoricoUsoDispositivoDao();
            base.GenericDao = Dao;
        }

        public override void Dispose()
        {
            base.Dispose();
            this.Dao.Dispose();
        }

        public override void Validar(HistoricoUsoDispositivo entity)
        {

        }

    }
}
