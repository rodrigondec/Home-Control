using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Domain.Dispositivos;
using HomeControl.Business.Service.Implementations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace HomeControl.Controllers
{
    public class EmbarcadoController : Controller
    {
        private IEmbarcadoService _embarcadoService = new EmbarcadoService();

        // GET: Embarcado
        public ActionResult Index()
        {
            return View(_embarcadoService.FindAll());
        }

        // GET: Embarcado/Details/5
        public ActionResult Details(int id)
        {

            Embarcado embarcado = _embarcadoService.Find(id);

            if (embarcado == null)
            {
                ModelState.AddModelError("", "Embarcado não encontrada");
                return RedirectToAction("Index");
            }

            return View(embarcado);
        }

        // GET: Embarcado/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Embarcado/Create
        [HttpPost]
        public ActionResult Create(Embarcado embarcado)
        {
            try
            {
                _embarcadoService.Add(embarcado);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(embarcado);
            }
        }

        // GET: Embarcado/Edit/5
        public ActionResult Edit(int id)
        {
            Embarcado embarcado = _embarcadoService.Find(id);

            if (embarcado == null)
            {
                ModelState.AddModelError("", "Embarcado não encontrada");
                return RedirectToAction("Index");
            }

            return View(embarcado);
        }

        // POST: embarcado/Edit/5
        [HttpPost]
        public ActionResult Edit(Embarcado embarcado)
        {
            try
            {
                _embarcadoService.Update(embarcado);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(embarcado);
            }
        }

        // GET: Embarcado/Delete/5
        public ActionResult Delete(int id)
        {
            return View();
        }

        // POST: Embarcado/Delete/5
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