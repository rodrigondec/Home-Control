using HomeControl.Domain.Dispositivos;
using HomeControl.Domain.Domain.Security;
using HomeControl.Domain.Residencia;
using Microsoft.AspNet.Identity.EntityFramework;
using System.Data.Entity;
using System;

namespace HomeControl.Data.Dal.Context
{
    public class HomeControlDBContext : IdentityDbContext<Usuario>
    {
       // public DbSet<Dispositivo> Dispositivos { get; set; }
        public DbSet<Embarcado> Embarcados { get; set; }
        public DbSet<Comodo> Comodos { get; set; }
        public DbSet<Residencia> Residencias { get; set; }

        public HomeControlDBContext() : base("DefaultConnection", throwIfV1Schema: false) { }

        public static HomeControlDBContext Create()
        {
            return new HomeControlDBContext();
        }
    }
}
