using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Implementations;
using HomeControl.Business.Service.Interfaces;
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

        private IResidenciaService service = new ResidenciaService();

        // GET: Residencia
        public ActionResult Index()
        {
            return View(service.FindAll());
        }

        // GET: Residencia/Details/5
        public ActionResult Details(int id)
        {

            Residencia casa = service.Find(id);

            if(casa == null)
            {
                ModelState.AddModelError("", "Residência não encontrada");
                return RedirectToAction("Index");
            }

            return View(casa);
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
            Residencia casa = service.Find(id);

            if (casa == null)
            {
                ModelState.AddModelError("", "Residência não encontrada");
                return RedirectToAction("Index");
            }

            return View(casa);
        }

        // POST: Residencia/Edit/5
        [HttpPost]
        public ActionResult Edit(Residencia residencia)
        {
            try
            {
                service.Update(residencia);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(residencia);
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
