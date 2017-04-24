using System;
using System.Net.Http;

namespace Rest.Clients
{
    public class RestClientException : Exception
    {
        public RestClientException(String message) : base(message) {}
    }
}