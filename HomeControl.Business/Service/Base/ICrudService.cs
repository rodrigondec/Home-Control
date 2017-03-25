using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Base.interfaces
{
    public interface ICrudService<T, ID> : IDisposable where T : class
    {
        List<T> FindAll();
        T Find(ID id);
        T Update(T entity);
        T Add(T entity);
        //void Validar(T entity);
    }
}