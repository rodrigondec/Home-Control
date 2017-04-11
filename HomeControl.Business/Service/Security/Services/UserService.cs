using HomeControl.Business.Service.Security.Managers;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Security
{
    public class UserService
    {
        private UserManager _userManager;
        public UserManager UserManager
        {
            get
            {
                return _userManager;
            }
            private set
            {
                _userManager = value;
            }
        }

        public UserService(UserManager userManager)
        {
            UserManager = userManager;
        }

        //Register
        //ConfirmEmail
        //ForgotPassword
        //ResetPassword
        //SendCode;
        //ExternalLoginConfirmation

    }
}
