﻿using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Implementation;
using HomeControl.Domain.Residencia;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace HomeControl.Controllers
{
    public class ResidenciaController : Controller
    {

        private ResidenciaService service = new ResidenciaService();

        // GET: Residencia
        public ActionResult Index()
        {
            return View(service.FindAll());
        }

        // GET: Residencia/Details/5
        public ActionResult Details(int id)
        {
            return View();
        }

        // GET: Residencia/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Residencia/Create
        [HttpPost]
        public ActionResult Create(Residencia residencia)
        {
            try
            {
                service.Add(residencia);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {                              
                AddValidationErrorsToModelState(ex.Errors);
                return View(residencia);
            }
        }

        // GET: Residencia/Edit/5
        public ActionResult Edit(int id)
        {
            return View();
        }

        // POST: Residencia/Edit/5
        [HttpPost]
        public ActionResult Edit(int id, FormCollection collection)
        {
            try
            {
                // TODO: Add update logic here

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: Residencia/Delete/5
        public ActionResult Delete(int id)
        {
            return View();
        }

        // POST: Residencia/Delete/5
        [HttpPost]
        public ActionResult Delete(int id, FormCollection collection)
        {
            try
            {
                // TODO: Add delete logic here

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        #region helpers
        private void AddValidationErrorsToModelState(ErrorList validationErrors)
        {
            foreach (String error in validationErrors.ErrorCodes)
            {
                ModelState.AddModelError("", error);
            }
        }

        #endregion
    }
}