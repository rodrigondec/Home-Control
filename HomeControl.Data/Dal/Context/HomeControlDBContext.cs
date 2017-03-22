using HomeControl.Domain.Dispositivos;
using HomeControl.Domain.Residencia;
using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Data.Dal.Context
{
    public class HomeControlDBContext : DbContext
    {

        public DbSet<Dispositivo> Dispositivos { get; set; }
        public DbSet<Controlador> Controladores { get; set; }
        public DbSet<Comodo> Comodos { get; set; }
        public DbSet<Residencia> Residencias { get; set; }

        public HomeControlDBContext() : base("DefaultConnection"){}

    }
}
