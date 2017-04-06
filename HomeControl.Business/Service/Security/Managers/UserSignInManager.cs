using HomeControl.Domain.Domain.Security;
using Microsoft.AspNet.Identity.Owin;
using Microsoft.Owin;
using Microsoft.Owin.Security;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Claims;
using System.Text;
using System.Threading.Tasks;

namespace HomeControl.Business.Service.Security.Managers
{
    public class UserSignInManager : SignInManager<Usuario, string>
    {

        public UserSignInManager(UserManager userManager, IAuthenticationManager authenticationManager)
            : base(userManager, authenticationManager)
        {
        }

        public override Task<ClaimsIdentity> CreateUserIdentityAsync(Usuario user)
        {
            return user.GenerateUserIdentityAsync((UserManager)UserManager);
        }

        public static UserSignInManager Create(IdentityFactoryOptions<UserSignInManager> options, IOwinContext context)
        {
            return new UserSignInManager(context.GetUserManager<UserManager>(), context.Authentication);
        }

    }
}
