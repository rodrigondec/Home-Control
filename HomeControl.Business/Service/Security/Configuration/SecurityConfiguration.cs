using HomeControl.Business.Service.Security.Managers;
using HomeControl.Data.Dal.Context;
using Microsoft.Owin;
using Owin;

namespace HomeControl.Business.Service.Security.Configuration
{
    public class SecurityConfiguration
    {
        public static void Configure(IAppBuilder applicationBuilder)
        {
            applicationBuilder.CreatePerOwinContext(HomeControlDBContext.Create);
            applicationBuilder.CreatePerOwinContext<UserManager>(UserManager.Create);
            applicationBuilder.CreatePerOwinContext<UserSignInManager>(UserSignInManager.Create);
            applicationBuilder.CreatePerOwinContext<UserService>(UserService.Create);
            applicationBuilder.CreatePerOwinContext<SignInService>(SignInService.Create);
            applicationBuilder.CreatePerOwinContext<SecurityFacade>(SecurityFacade.Create);            
        }

    }
}
