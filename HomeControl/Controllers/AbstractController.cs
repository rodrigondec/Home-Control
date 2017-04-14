using HomeControl.Business.Service.Security;
using HomeControl.Domain.Domain.Security;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace HomeControl.Controllers
{
    public abstract class AbstractController : Controller
    {
        public SecurityFacade _securityFacade;
        public UserService _userService;

        public AbstractController(SecurityFacade securityFacade, UserService userService)
        {
            _securityFacade = securityFacade;
            _userService = userService;
        }

        public Usuario GetCurrentUser()
        {
            return null;
            //return User.Identity.Name;
        }
    }
}