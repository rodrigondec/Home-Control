using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Implementations;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Domain.Residencia;
using Ninject;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace HomeControl.Controllers
{
    public class ComodoController : Controller
    {
        private IComodoService _comodoService = new ComodoService();
        private IResidenciaService _residenciaService = new ResidenciaService();

        [Inject]
        public ComodoController(IResidenciaService residenciaService, IComodoService comodoService)
        {
            _residenciaService = residenciaService;
            _comodoService = comodoService;
        }      

        // GET: Comodo
        public ActionResult Index()
        {
            return View(_comodoService.FindAll());
        }

        // GET: Comodo/Details/5
        public ActionResult Details(int id)
        {

            Comodo comodo = _comodoService.Find(id);

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
            PopulateSelectListResidencia();
            return View();
        }

        // POST: Comodo/Create
        [HttpPost]
        public ActionResult Create(Comodo comodo)
        {
            try
            {
                _comodoService.Add(comodo);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                PopulateSelectListResidencia();
                AddValidationErrorsToModelState(ex.Errors);
                return View(comodo);
            }
        }

        // GET: Comodo/Edit/5
        public ActionResult Edit(int id)
        {
            Comodo comodo = _comodoService.Find(id);

            if (comodo == null)
            {
                ModelState.AddModelError("", "Cômodo não encontrada");
                return RedirectToAction("Index");
            }

            PopulateSelectListResidencia();
            return View(comodo);
        }

        // POST: Comodo/Edit/5
        [HttpPost]
        public ActionResult Edit(Comodo comodo)
        {
            try
            {
                _comodoService.Update(comodo);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                PopulateSelectListResidencia();
                AddValidationErrorsToModelState(ex.Errors);
                return View(comodo);
            }
        }

        // GET: Comodo/Delete/5
        public ActionResult Delete(int id)
        {
            Comodo comodo = _comodoService.Find(id);
            if(comodo == null)
            {
                ModelState.AddModelError("", "Comodo não Encontrado");
                return RedirectToAction("Index");
            }
            return View(comodo);
        }

        // POST: Comodo/Delete/5
        [HttpPost]
        public ActionResult Delete(Comodo comodo)
        {
            try
            {
                comodo = _comodoService.Find(comodo.Id);
                _comodoService.Remove(comodo);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(comodo);
            }
        }

        private void PopulateSelectListResidencia()
        {
            List<Residencia> residencias = _residenciaService.FindAll();
            SelectList listaOpcoesResidencia = new SelectList(residencias, "id", "Nome");
            ViewBag.SelectListResidencia = listaOpcoesResidencia;
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