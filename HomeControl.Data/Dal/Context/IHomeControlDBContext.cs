using System.Data.Entity;
using HomeControl.Domain.Dispositivos;
using HomeControl.Domain.Residencia;
using System;

namespace HomeControl.Data.Dal.Context
{
    public interface IHomeControlDBContext: IDisposable
    {
        DbSet<Comodo> Comodos { get; set; }
        DbSet<Dispositivo> Dispositivos { get; set; }
        DbSet<Embarcado> Embarcados { get; set; }
        DbSet<Residencia> Residencias { get; set; }
    }
}