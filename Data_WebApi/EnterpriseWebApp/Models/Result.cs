using Newtonsoft.Json;

namespace EnterpriseWebApp.Models
{
    public class Result
    {
        public sealed class Ok<T> : Result
        {
            public Ok(T data)
            {
                this.ResultData = data;
            }

            public int StatusCode { get => 1; }

            public T ResultData { get; set; }
        }

        public sealed class Error : Result
        {
            public Error(string error, int statusCode = -1)
            {
                this.ErrorMessage = error;
                this.StatusCode = statusCode;
            }

            public int StatusCode { get; set; }

            public string ErrorMessage { get; set; }
        }

        public static Result CombineResult<T>(
            Result result1,
            Result result2,
            Func<Ok<T>, Ok<T>, Result> SuccessCombiner = null)
        {
            return (result1, result2) switch
            {
                (Ok<T> r1, Ok<T> r2) => SuccessCombiner is null ? r2 : SuccessCombiner(r1, r2),
                (Ok<T> _, Error e2) => e2,
                (Error e1, Ok<T> _) => e1,
                (Error e1, Error e2) => new Error(e1.ErrorMessage + Environment.NewLine + e2.ErrorMessage),
                _ => throw new NotImplementedException()
            };
        }

        [JsonIgnore]
        public readonly Func<Result.Ok<bool>, Result.Ok<bool>, Result> OkCombiner = (r1, r2) =>
             new Result.Ok<bool>(r1.ResultData && r2.ResultData);
    }
}
