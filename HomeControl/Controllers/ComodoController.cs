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
    public class ComodoController : Controller
    {
        private IComodoService service = new ComodoService();

        // GET: Comodo
        public ActionResult Index()
        {
            return View(service.FindAll());
        }

        // GET: Comodo/Details/5
        public ActionResult Details(int id)
        {

            Comodo comodo = service.Find(id);

            if (comodo == null)
            {
                ModelState.AddModelError("", "Cômodo não encontrada");
                return RedirectToAction("Index");
            }

            return View(comodo);
        }

        // GET: Comodo/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Comodo/Create
        [HttpPost]
        public ActionResult Create(Comodo comodo)
        {
            try
            {
                service.Add(comodo);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(comodo);
            }
        }

        // GET: Comodo/Edit/5
        public ActionResult Edit(int id)
        {
            Comodo comodo = service.Find(id);

            if (comodo == null)
            {
                ModelState.AddModelError("", "Cômodo não encontrada");
                return RedirectToAction("Index");
            }

            return View(comodo);
        }

        // POST: Comodo/Edit/5
        [HttpPost]
        public ActionResult Edit(Comodo comodo)
        {
            try
            {
                service.Update(comodo);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(comodo);
            }
        }

        // GET: Comodo/Delete/5
        public ActionResult Delete(int id)
        {
            return View();
        }

        // POST: Comodo/Delete/5
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