using HomeControl.Domain.Dispositivos;
using HomeControl.Domain.Domain.Security;
using HomeControl.Domain.Residencia;
using Microsoft.AspNet.Identity.EntityFramework;
using System.Data.Entity;
using System;
using System.Data.Common;

namespace HomeControl.Data.Dal.Context
{
    public class HomeControlDBContext : IdentityDbContext<Usuario>, IHomeControlDBContext
    {
        public DbSet<Dispositivo> Dispositivos { get; set; }
        public DbSet<Embarcado> Embarcados { get; set; }
        public DbSet<Comodo> Comodos { get; set; }
        public DbSet<Residencia> Residencias { get; set; }

        public HomeControlDBContext() : base("DefaultConnection", throwIfV1Schema: false) { }

        public HomeControlDBContext(DbConnection connection) : base(connection, true)
        {
            this.Configuration.LazyLoadingEnabled = false;
        }

        public HomeControlDBContext(string nameOrConnectionString) : base(nameOrConnectionString)
        {
            this.Configuration.LazyLoadingEnabled = false;
        }

        public static HomeControlDBContext Create()
        {
            return new HomeControlDBContext();
        }
    }
}
