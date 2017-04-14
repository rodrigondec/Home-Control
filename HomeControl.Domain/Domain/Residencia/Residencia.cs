using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace HomeControl.Domain.Residencia
{
    public class Residencia : IPersistable<int>
    {
        [Key]       
        private int id;
        private String nome;
        private HashSet<Comodo> comodos;
        
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
        public HashSet<Comodo> Comodos
        {
            get
            {
                return this.comodos;
            }
            set
            {
                this.comodos = value;
            }
        }

    }
}