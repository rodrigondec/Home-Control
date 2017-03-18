using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace HomeControl.Domain.Dispositivos
{
    public class Controlador : Activable
    {
       
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
        [Display(Name = "Nome")]
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
        [Display(Name = "Endereço ip")]
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
        [Display(Name = "Endereço Mac")]
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