using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace HomeControl.Domain.Dispositivos
{
    public class Embarcado : IActivable, IPersistable<int>
    {
        [Key]
        private int id;
        private String nome;
        private String socket;
        private String macAddress;
        private HashSet<Dispositivo> dispositivos;

       
        public int Id
        {
            get
            {
                return id;
            }

            set
            {
                id = value;
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

        public String Socket
        {
            get
            {
                return this.socket;
            }
            set
            {
                this.socket = value;
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

        public HashSet<Dispositivo> Dispositivos
        {
            get
            {
                return this.dispositivos;
            }
            set
            {
                this.dispositivos = value;
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