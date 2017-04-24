using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace Rest.Clients
{
    public class BaseClient
    {
        public HttpClient Client { get; set; }

        public BaseClient()
        {
            Client = new HttpClient();
        }

        public String GetResultSynchronously(string uri)
        {
            var task = GetResultAsynchronously(uri);          

            return task.Result;
        }

        public async Task<String> GetResultAsynchronously(string uri)
        {
            var result = await Client.GetAsync(uri);

            if (!result.IsSuccessStatusCode)
            {
                throw new RestClientException("Erro ao executar a operação GET");
            }

            var content = await result.Content.ReadAsStringAsync();

            return content;
        }

        public T DesserializeContent<T>(String content)
        {
            return JsonConvert.DeserializeObject<T>(content, new JsonSerializerSettings()
            {
                MissingMemberHandling = MissingMemberHandling.Ignore
            });
        }

    }
}
