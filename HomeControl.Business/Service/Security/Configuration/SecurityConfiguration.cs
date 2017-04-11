using HomeControl.Business.Service.Security.Managers;
using HomeControl.Data.Dal.Context;
using Microsoft.Owin;
using Owin;

namespace HomeControl.Business.Service.Security.Configuration
{
    public class SecurityConfiguration
    {
        public static void Configure(IAppBuilder app)
        {
            app.CreatePerOwinContext(HomeControlDBContext.Create);
            app.CreatePerOwinContext<UserManager>(UserManager.Create);
            app.CreatePerOwinContext<UserSignInManager>(UserSignInManager.Create);
            app.CreatePerOwinContext<SignInService>(SignInService.Create);
            app.CreatePerOwinContext<SecurityFacade>(SecurityFacade.Create);            
        }

    }
}
