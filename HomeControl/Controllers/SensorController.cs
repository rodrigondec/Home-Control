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

        private ISensorService _sensorService = new SensorService();

        // GET: Sensor
        public ActionResult Index()
        {
            return View(_sensorService.FindAll());
        }

        // GET: Sensor/Details/5
        public ActionResult Details(int id)
        {
            Sensor sensor = _sensorService.Find(id);

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
                _sensorService.Add(sensor);

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
            Sensor sensor = _sensorService.Find(id);

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
                _sensorService.Update(sensor);

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
            Sensor sensor = _sensorService.Find(id);
            if(sensor == null)
            {
                ModelState.AddModelError("", "Sensor não Encontrado");
                return RedirectToAction("Index");
            }
            return View(sensor);
        }

        // POST: Sensor/Delete/5
        [HttpPost]
        public ActionResult Delete(Sensor sensor)
        {
            try
            {
                sensor = _sensorService.Find(sensor.Id);
                _sensorService.Remove(sensor);

                return RedirectToAction("Index");
            }
            catch (BusinessException ex)
            {
                AddValidationErrorsToModelState(ex.Errors);
                return View(sensor);
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
