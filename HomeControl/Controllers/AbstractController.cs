using HomeControl.Business.Service.Base.Exceptions;
using HomeControl.Business.Service.Security;
using HomeControl.Domain.Domain.Security;
using Ninject;
using System;
using System.Web.Mvc;

namespace HomeControl.Controllers
{
    public abstract class AbstractController : Controller
    {
        [Inject]
        public SecurityFacade _securityFacade { get; set; }
        public UserService _userService { get; set; }

        public Usuario GetCurrentUser()
        {
            return _userService.FindByNameAsync(User.Identity.Name).Result;          
        }

        protected void AddValidationErrorsToModelState(ErrorList validationErrors)
        {
            foreach (String error in validationErrors.ErrorCodes)
            {
                ModelState.AddModelError("", error);
            }
        }
    }
}