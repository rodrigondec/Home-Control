using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Implementations;
using HomeControl.Domain.Interruptores;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace HomeControl.Controllers
{
    public class InterruptorController : Controller
    {
        private InterruptorService service = new InterruptorService();

        // GET: Interruptor
        public ActionResult Index()
        {
            return View(service.FindAll());
        }

        // GET: Interruptor/Details/5
        public ActionResult Details(int id)
        {

            Interruptor interruptor = service.Find(id);

            if (interruptor == null)
            {
                ModelState.AddModelError("", "Interruptor não encontrada");
                return RedirectToAction("Index");
            }

            return View(interruptor);
        }

        // GET: Interruptor/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Interruptor/Create
        [HttpPost]
        public ActionResult Create(Interruptor Interruptor)
        {
            try
            {
                service.Add(Interruptor);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(Interruptor);
            }
        }

        // GET: Interruptor/Edit/5
        public ActionResult Edit(int id)
        {
            Interruptor interruptor = service.Find(id);

            if (interruptor == null)
            {
                ModelState.AddModelError("", "Interruptor não encontrada");
                return RedirectToAction("Index");
            }

            return View(interruptor);
        }

        // POST: Interruptor/Edit/5
        [HttpPost]
        public ActionResult Edit(Interruptor Interruptor)
        {
            try
            {
                service.Update(Interruptor);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(Interruptor);
            }
        }

        // GET: Interruptor/Delete/5
        public ActionResult Delete(int id)
        {
            return View();
        }

        // POST: Interruptor/Delete/5
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