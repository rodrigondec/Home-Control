using HomeControl.Domain.Residencia;
using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace HomeControl.Domain.Dispositivos
{
    public abstract class Dispositivo : Activable
    {
        [Key]
        private int id;
        [NotMapped]
        private Boolean ativo;
        private int porta;
        private int estado;
        private Comodo comodo;

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
        public Boolean Ativo
        {
            get
            {
                return this.ativo;
            }
            set
            {
                this.ativo = value;
            }
        }
        public int Porta
        {
            get
            {
                return this.porta;
            }
            set
            {
                this.porta = value;
            }
        }
        public int Estado
        {
            get
            {
                return this.estado;
            }
            set
            {
                this.estado = value;
            }
        }

        public Comodo Comodo
        {
            get
            {
                return comodo;
            }

            set
            {
                comodo = value;
            }
        }

        public abstract void activate();

        public abstract void deactivate();     

        public abstract bool isActive();        
    }
}