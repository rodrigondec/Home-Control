using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Implementations;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Domain.Dispositivos;
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
        private IEmbarcadoService _embarcadoService;

        [Inject]
        public InterruptorController(IInterruptorService interruptorService, IComodoService comodoService, IEmbarcadoService embarcadoService)
        {
            _interruptorService = interruptorService;
            _comodoService = comodoService;
            _embarcadoService = embarcadoService;
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
            Interruptor interruptor = _interruptorService.Find(id);
            if(interruptor == null)
            {
                ModelState.AddModelError("", "Interruptor não Encontrado");
                return RedirectToAction("Index");
            }
            return View(interruptor);
        }

        // POST: Interruptor/Delete/5
        [HttpPost]
        public ActionResult Delete(Interruptor interruptor)
        {
            try
            {
                interruptor = _interruptorService.Find(interruptor.Id);
                _interruptorService.Remove(interruptor);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(interruptor);
            }
        }
        
        private void PopulateSelectListComodo()
        {
            List<Comodo> comodos = _comodoService.FindAll();
            SelectList listaOpcoesComodo = new SelectList(comodos, "id", "Nome");
            ViewBag.SelectListComodo = listaOpcoesComodo;

            List<Embarcado> embarcados = _embarcadoService.FindAll();
            SelectList listaOpcoesEmbarcado = new SelectList(embarcados, "id", "Nome");
            ViewBag.SelectListEmbarcado = listaOpcoesEmbarcado;
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