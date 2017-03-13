using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(HomeControl.Startup))]
namespace HomeControl
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
