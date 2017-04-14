using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace HomeControl.Domain.Residencia
{
    public class Comodo : IPersistable<int>
    {
        [Key]
        private int id;
        private string nome;

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

        public string Nome
        {
            get
            {
                return nome;
            }

            set
            {
                nome = value;
            }
        }

       
        public int ResidenciaId { get; set; }
        [ForeignKey("ResidenciaId")]
        public virtual Residencia Residencia
        {
            get; protected set;
        }
    }
}