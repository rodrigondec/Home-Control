using System.Collections.Generic;
using System.Threading.Tasks;
using HomeControl.Domain.Domain.Security;
using Microsoft.AspNet.Identity;
using Microsoft.AspNet.Identity.Owin;
using System;

namespace HomeControl.Business.Service.Security
{
    public interface ISecurityFacade : IDisposable
    {
        Task<bool> HasBeenVerifiedAsync();
        Task Login(Usuario user, bool rememberMe, bool shouldLockout);
        Task<SignInStatus> Login(string email, string password, bool rememberMe, bool shouldLockout);
        Task<SignInStatus> VerifyCode(string provider, string code, bool isPersistent, bool rememberBrowser);
        Task<IdentityResult> AddLoginAsync(string userId, UserLoginInfo login);
        Task<IdentityResult> ConfirmEmailAsync(string userId, string code);
        Task<IdentityResult> CreateAsync(Usuario user);
        Task<IdentityResult> CreateAsync(Usuario user, string Password);
        Task<Usuario> FindByNameAsync(string name);
        Task<IList<string>> GetValidTwoFactorProvidersAsync(string userId);
        Task<bool> IsEmailConfirmedAsync(string userId);
        Task<IdentityResult> ResetPasswordAsync(string userId, string code, string password);
        Task<SignInStatus> ExternalSignInAsync(ExternalLoginInfo loginInfo, bool isPersistent);
        Task<string> GetVerifiedUserIdAsync();
        Task<bool> SendTwoFactorCodeAsync(string selectedProvider);
    }
}