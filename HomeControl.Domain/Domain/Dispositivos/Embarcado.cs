using System;
using System.ComponentModel.DataAnnotations;

namespace HomeControl.Domain.Dispositivos
{
    public class Embarcado : IActivable, IPersistable<int>
    {
       
             
         private String nome;       
         private String ipAddress;        
         private String macAddress;

       [Key]
       public int Id
        {
            get;

            set;
        }

        public String Nome
         {
             get
             {
                 return this.nome;
             }
             set
             {
                 this.nome = value;
             }
         }
     
         public String IpAddress
         {
             get
             {
                 return this.ipAddress;
             }
             set
             {
                 this.ipAddress = value;
             }
         }
  
         public String MacAddress
         {
             get
             {
                 return this.macAddress;
             }
             set
             {
                 this.macAddress = value;
             }
         }   

        void validarDispositivos()
        {
            throw new NotImplementedException();
        }

        public void Activate()
        {
            throw new NotImplementedException();
        }

        public void Deactivate()
        {
            throw new NotImplementedException();
        }

        public bool IsActive()
        {
            throw new NotImplementedException();
        }
    }
}