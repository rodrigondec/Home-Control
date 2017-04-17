using System.Collections.Generic;
using System.Threading.Tasks;
using HomeControl.Business.Service.Security.Managers;
using HomeControl.Domain.Domain.Security;
using Microsoft.AspNet.Identity;

namespace HomeControl.Business.Service.Security
{
    public interface IUserService
    {
        Task<IdentityResult> AddLoginAsync(string userId, UserLoginInfo login);
        Task<IdentityResult> ConfirmEmailAsync(string userId, string code);
        Task<IdentityResult> CreateAsync(Usuario user);
        Task<IdentityResult> CreateAsync(Usuario user, string Password);
        void Dispose();
        Task<Usuario> FindByNameAsync(string name);
        Task<IList<string>> GetValidTwoFactorProvidersAsync(string userId);
        Task<bool> IsEmailConfirmedAsync(string userId);
        Task<IdentityResult> ResetPasswordAsync(string userId, string code, string password);
    }
}