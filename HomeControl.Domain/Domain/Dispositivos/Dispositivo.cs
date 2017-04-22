using HomeControl.Domain.Residencia;
using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace HomeControl.Domain.Dispositivos
{
    public abstract class Dispositivo : IActivable, IPersistable<int>
    {
        [Key]
        private int id;
        [NotMapped]
        private Boolean ativo;
        private int porta;
        private int estado;

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

        public int ComodoId { get; set; }
        [ForeignKey("ComodoId")]
        public virtual Comodo Comodo { get; protected set; }

        public int Embarcadoid { get; set; }
        [ForeignKey("Embarcadoid")]
        public virtual Embarcado Embarcado { get; protected set; }

        public abstract void Activate();

        public abstract void Deactivate();

        public abstract bool IsActive();
    }
}