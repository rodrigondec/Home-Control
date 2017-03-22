using System;
using System.ComponentModel.DataAnnotations;

namespace HomeControl.Domain.Dispositivos
{
    public class Controlador : Activable
    {
        [Key]
        private int id;       
        private String nome;       
        private String ipAddress;        
        private String macAddress;

        public int Id
        {
            get
            {
                return this.id;
            }
            set
            {
                this.id = value;
            }
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

        public void activate()
        {
            throw new NotImplementedException();
        }

        public void deactivate()
        {
            throw new NotImplementedException();
        }

        public bool isActive()
        {
            throw new NotImplementedException();
        }
    }
}