using HomeControl.Business.Service.Security.Managers;
using HomeControl.Domain.Domain.Security;
using Microsoft.AspNet.Identity.Owin;
using Microsoft.Owin;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Security
{
    public class SignInService : ISignInService
    {
        public UserSignInManager _signinManager;      

        public SignInService(UserSignInManager signInManager)
        {
            this._signinManager = signInManager;
        }
             
        public Task<SignInStatus> Login(String email, String password, bool rememberMe, bool shouldLockout)
        {
            return _signinManager.PasswordSignInAsync(email, password, rememberMe, shouldLockout);           
        }

        public Task Login(Usuario user, bool rememberMe, bool shouldLockout)
        {
            return _signinManager.SignInAsync(user, isPersistent: false, rememberBrowser: false); ;
        }

        public Task<bool> HasBeenVerifiedAsync()
        {
            return _signinManager.HasBeenVerifiedAsync();
        }

         public Task<SignInStatus> VerifyCode(String provider,String code, bool isPersistent, bool rememberBrowser) {
            return _signinManager.TwoFactorSignInAsync(provider, code, isPersistent, rememberBrowser);
         }

        public static SignInService Create(IdentityFactoryOptions<SignInService> options, IOwinContext context)
        {
            return new SignInService(context.Get<UserSignInManager>());
        }

        public void Dispose()
        {
            _signinManager.Dispose();
        }

        //        Login
        //        VerifyCode

        //SendCode
        //ExternalLoginCallBack
        //ExternalLoginConfirmation
    }
}
