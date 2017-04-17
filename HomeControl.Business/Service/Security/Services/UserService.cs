using HomeControl.Business.Service.Security.Managers;
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
    public class UserService : IDisposable, IUserService
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

        public static UserService Create(IdentityFactoryOptions<UserService> options, IOwinContext context)
        {           
            return new UserService(context.Get<UserManager>());
        }

        public UserService(UserManager userManager)
        {
            UserManager = userManager;
        }
        public Task<IdentityResult> AddLoginAsync(String userId,UserLoginInfo login)
        {
            return UserManager.AddLoginAsync(userId, login);
        }     

        public Task<IdentityResult> CreateAsync(Usuario user)
        {
            return UserManager.CreateAsync(user);
        }       

        public Task<IdentityResult> CreateAsync(Usuario user,string Password) {
           return UserManager.CreateAsync(user, Password);
        }
        public Task<IdentityResult> ConfirmEmailAsync(string userId, string code)
        {
            return UserManager.ConfirmEmailAsync(userId, code);
        }
        public Task<Usuario> FindByNameAsync(string name)
        {
            return UserManager.FindByNameAsync(name);
        }
        public Task<bool> IsEmailConfirmedAsync(string userId)
        {
            return UserManager.IsEmailConfirmedAsync(userId);
        }
        

        public Task<IdentityResult> ResetPasswordAsync(string userId, string code, string password)
        {
            return UserManager.ResetPasswordAsync(userId, code, password);
        }

        public Task<IList<String>>GetValidTwoFactorProvidersAsync(string userId)
        {
            return UserManager.GetValidTwoFactorProvidersAsync(userId);
        }

        public void Dispose()
        {
            UserManager.Dispose();
        }
    }
}
