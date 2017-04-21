using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Implementations;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Domain.Interruptores;
using HomeControl.Domain.Residencia;
using Ninject;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace HomeControl.Controllers
{
    public class InterruptorController : Controller
    {
        private IInterruptorService _interruptorService;
        private IComodoService _comodoService;

        [Inject]
        public InterruptorController(IInterruptorService interruptorService, IComodoService comodoService)
        {
            _interruptorService = interruptorService;
            _comodoService = comodoService;
        }

        // GET: Interruptor
        public ActionResult Index()
        {
            return View(_interruptorService.FindAll());
        }

        // GET: Interruptor/Details/5
        public ActionResult Details(int id)
        {

            Interruptor interruptor = _interruptorService.Find(id);

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
            PopulateSelectListComodo();
            return View();
        }

        // POST: Interruptor/Create
        [HttpPost]
        public ActionResult Create(Interruptor Interruptor)
        {
            try
            {
                _interruptorService.Add(Interruptor);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                PopulateSelectListComodo();
                AddValidationErrorsToModelState(ex.Errors);
                return View(Interruptor);
            }
        }

        // GET: Interruptor/Edit/5
        public ActionResult Edit(int id)
        {
            Interruptor interruptor = _interruptorService.Find(id);
            PopulateSelectListComodo();
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
                _interruptorService.Update(Interruptor);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                PopulateSelectListComodo();
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
        
        private void PopulateSelectListComodo()
        {
            List<Comodo> comodos = _comodoService.FindAll();
            SelectList listaOpcoesComodo = new SelectList(comodos, "id", "Nome");
            ViewBag.SelectListComodo = listaOpcoesComodo;
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