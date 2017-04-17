using System.Threading.Tasks;
using HomeControl.Domain.Domain.Security;
using Microsoft.AspNet.Identity.Owin;
using System;

namespace HomeControl.Business.Service.Security
{
    public interface ISignInService : IDisposable
    {
        Task<SignInStatus> ExternalSignInAsync(ExternalLoginInfo loginInfo, bool isPersistent);
        Task<string> GetVerifiedUserIdAsync();
        Task<bool> HasBeenVerifiedAsync();
        Task Login(Usuario user, bool rememberMe, bool shouldLockout);
        Task<SignInStatus> Login(string email, string password, bool rememberMe, bool shouldLockout);
        Task<bool> SendTwoFactorCodeAsync(string selectedProvider);
        Task<SignInStatus> VerifyCode(string provider, string code, bool isPersistent, bool rememberBrowser);
    }
}