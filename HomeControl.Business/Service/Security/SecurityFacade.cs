using HomeControl.Domain.Domain.Security;
using Microsoft.AspNet.Identity;
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
        public UserService _userService;

        public SecurityFacade(SignInService signInService, UserService userService)
        {
            _signInService = signInService;
            _userService = userService;
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
            return _signInService.VerifyCode(provider, code, isPersistent, rememberBrowser);
        }

        public Task<IdentityResult> AddLoginAsync(string userId, UserLoginInfo login)
        {
            return _userService.AddLoginAsync(userId, login);
        }

        public Task<IdentityResult> ConfirmEmailAsync(string userId, string code)
        {
            return _userService.ConfirmEmailAsync(userId, code);
        }

        public Task<IdentityResult> CreateAsync(Usuario user)
        {
            return _userService.CreateAsync(user);
        }

        public Task<IdentityResult> CreateAsync(Usuario user, string Password)
        {
            return _userService.CreateAsync(user, Password);
        }

        public Task<Usuario> FindByNameAsync(string name)
        {
            return _userService.FindByNameAsync(name);
        }

        public Task<IList<string>> GetValidTwoFactorProvidersAsync(string userId)
        {
            return _userService.GetValidTwoFactorProvidersAsync(userId);
        }

        public Task<bool> IsEmailConfirmedAsync(string userId)
        {
            return _userService.IsEmailConfirmedAsync(userId);
        }

        public Task<IdentityResult> ResetPasswordAsync(string userId, string code, string password)
        {
            return _userService.ResetPasswordAsync(userId, code, password);
        }
        public Task<SignInStatus> ExternalSignInAsync(ExternalLoginInfo loginInfo, bool isPersistent)
        {
            return _signInService.ExternalSignInAsync(loginInfo, isPersistent);
        }
        public Task<string> GetVerifiedUserIdAsync()
        {
            return _signInService.GetVerifiedUserIdAsync();
        }

        public Task<bool> SendTwoFactorCodeAsync(string selectedProvider)
        {
            return _signInService.SendTwoFactorCodeAsync(selectedProvider);
        }
        public static SecurityFacade Create(IdentityFactoryOptions<SecurityFacade> options, IOwinContext context)
        {
            SignInService signInService = context.Get<SignInService>();
            UserService userService = context.Get<UserService>();
            return new SecurityFacade(signInService, userService);
        }

        public void Dispose()
        {
            _signInService.Dispose();
            _userService.Dispose();
        }

    }
}
