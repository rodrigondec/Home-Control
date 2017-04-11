using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Base.interfaces
{
    /// <summary>
    /// Interface que define o contrato comum de um serviço crud.
    /// </summary>
    /// <typeparam name="T">Classe da entidade gerenciada pela implementação do crud.</typeparam>
    /// <typeparam name="ID">Tipo da chave primária.</typeparam>
    public interface ICrudService<T, ID> : IDisposable where T : class
    {
        List<T> FindAll();
        T Find(ID id);
        T Update(T entity);
        T Add(T entity);
        T Remove(T entity);        
        //void Validar(T entity);
    }
}