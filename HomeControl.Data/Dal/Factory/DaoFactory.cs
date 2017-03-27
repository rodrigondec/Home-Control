﻿using HomeControl.Data.Dal.Dao.Custom.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Data.Dal.Factory
{
    public abstract class DaoFactory
    {

        public abstract IComodoDao GetComodoDao(); 
        public abstract IControladorDao GetControladorDao(); 
        public abstract IDispositivoDao GetDispositivoDao();
        public abstract IResidenciaDao GetResidenciaDao();

    }
}