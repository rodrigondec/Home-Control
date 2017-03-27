using HomeControl.Domain.Dispositivos;
using HomeControl.Domain.Residencia;
using Microsoft.AspNet.Identity.EntityFramework;
using System.Data.Entity;

namespace HomeControl.Data.Dal.Context
{
    public class HomeControlDBContext : IdentityDbContext<IdentityUser>
    {
       // public DbSet<Dispositivo> Dispositivos { get; set; }
        public DbSet<Controlador> Controladores { get; set; }
        public DbSet<Comodo> Comodos { get; set; }
        public DbSet<Residencia> Residencias { get; set; }

        public HomeControlDBContext() : base("DefaultConnection") { }

    }
}
