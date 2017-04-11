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
    public class SecurityFacade : IDisposable
    {
        public SignInService _signInService;

        public SecurityFacade(SignInService signInService)
        {
            _signInService = signInService;
        }
       public Task<bool> HasBeenVerifiedAsync()
        {
            return _signInService.HasBeenVerifiedAsync();
        }
        public Task Login(Usuario user, bool rememberMe, bool shouldLockout)
        {
            return _signInService.Login(user, rememberMe, shouldLockout);
        }
        public Task<SignInStatus> Login(string email, string password, bool rememberMe, bool shouldLockout)
        {
            return _signInService.Login(email, password, rememberMe, shouldLockout);                
        }
        public Task<SignInStatus> VerifyCode(string provider, string code, bool isPersistent, bool rememberBrowser)
        {
            return _signInService.VerifyCode(provider,code,isPersistent,rememberBrowser);
        }
        
        public static SecurityFacade Create(IdentityFactoryOptions<SecurityFacade> options, IOwinContext context)
        {
            SignInService signInService = context.Get<SignInService>();

            return new SecurityFacade(signInService);
            
        }       
       
        public void Dispose()
        {
            _signInService.Dispose();
        }
               
    }
}
