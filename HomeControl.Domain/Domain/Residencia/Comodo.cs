using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace HomeControl.Domain.Residencia
{
    public class Comodo : IPersistable<int>
    {
        [Key]
        private int id;
        private string nome;
        private Residencia residencia;

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

        public Residencia Residencia
        {
            get
            {
                return residencia;
            }

            set
            {
                residencia = value;
            }
        }
    }
}