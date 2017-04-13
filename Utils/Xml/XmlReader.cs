namespace Utils.Xml
{
    public class XmlReader
    {
        public static string GetAppSettingUsingConfigurationManager(string customField)
        {
            return System.Configuration.ConfigurationManager.AppSettings[customField];
        }

        public static string GetAppSetting(string customField)
        {
            System.Configuration.Configuration config =
                System.Web.Configuration.WebConfigurationManager.OpenWebConfiguration(null);
            if (config.AppSettings.Settings.Count > 0)
            {
                var customSetting = config.AppSettings.Settings[customField].ToString();
                if (!string.IsNullOrEmpty(customSetting))
                {
                    return customSetting;
                }
            }
            return null;
        }
    }
}
