using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Implementations;
using HomeControl.Business.Service.Interfaces;
using HomeControl.Domain.Sensores;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace HomeControl.Controllers
{
    public class SensorController : Controller
    {

        private ISensorService service = new SensorService();

        // GET: Sensor
        public ActionResult Index()
        {
            return View(service.FindAll());
        }

        // GET: Sensor/Details/5
        public ActionResult Details(int id)
        {
            Sensor sensor = service.Find(id);

            if(sensor == null)
            {
                ModelState.AddModelError("", "Sensor não encontrada");
                return RedirectToAction("Index");
            }

            return View(sensor);
        }

        // GET: Sensor/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Sensor/Create
        [HttpPost]
        public ActionResult Create(Sensor sensor)
        {
            try
            {
                service.Add(sensor);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(sensor);
            }
        }

        // GET: Sensor/Edit/5
        public ActionResult Edit(int id)
        {
            Sensor sensor = service.Find(id);

            if (sensor == null)
            {
                ModelState.AddModelError("", "Sensor não encontrada");
                return RedirectToAction("Index");
            }

            return View(sensor);
        }

        // POST: Sensor/Edit/5
        [HttpPost]
        public ActionResult Edit(Sensor sensor)
        {
            try
            {
                service.Update(sensor);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(sensor);
            }
        }

        // GET: Sensor/Delete/5
        public ActionResult Delete(int id)
        {
            return View();
        }

        // POST: Sensor/Delete/5
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
