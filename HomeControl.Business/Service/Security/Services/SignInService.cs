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
        public UserSignInManager _signInManager;      

        public SignInService(UserSignInManager signInManager)
        {
            this._signInManager = signInManager;
        }
             
        public Task<SignInStatus> Login(String email, String password, bool rememberMe, bool shouldLockout)
        {
            return _signInManager.PasswordSignInAsync(email, password, rememberMe, shouldLockout);           
        }

        public Task Login(Usuario user, bool rememberMe, bool shouldLockout)
        {
            return _signInManager.SignInAsync(user, rememberMe, shouldLockout); 
        }

        public Task<bool> HasBeenVerifiedAsync()
        {
            return _signInManager.HasBeenVerifiedAsync();
        }

         public Task<SignInStatus> VerifyCode(String provider,String code, bool isPersistent, bool rememberBrowser) {
            return _signInManager.TwoFactorSignInAsync(provider, code, isPersistent, rememberBrowser);
         }

        public static SignInService Create(IdentityFactoryOptions<SignInService> options, IOwinContext context)
        {
            return new SignInService(context.Get<UserSignInManager>());
        }

        public void Dispose()
        {
            _signInManager.Dispose();
        }

        public Task<string> GetVerifiedUserIdAsync()
        {
            return _signInManager.GetVerifiedUserIdAsync();
        }

        public Task<bool> SendTwoFactorCodeAsync(string selectedProvider)
        {
            return _signInManager.SendTwoFactorCodeAsync(selectedProvider);
        }

        public Task ExternalSignInAsync(ExternalLoginInfo loginInfo, bool isPersistent)
        {
            return _signInManager.ExternalSignInAsync(loginInfo, isPersistent: false);
        }

        //        Login
        //        VerifyCode

        //SendCode
        //ExternalLoginCallBack
        //ExternalLoginConfirmation
    }
}
