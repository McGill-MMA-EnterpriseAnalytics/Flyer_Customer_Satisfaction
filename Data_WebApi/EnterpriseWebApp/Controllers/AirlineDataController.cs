using System.Data;
using EnterpriseWebApp.Data;
using Microsoft.AspNetCore.Mvc;
using EnterpriseWebApp.Models.ETL;
using Extract = EnterpriseWebApp.Models.Extract;

namespace EnterpriseWebApp.Controllers.ETL
{
    [ApiController]
    [Route("api/etl/[controller]")]
    public class AirlineDataController : ControllerBase
    {
        private readonly ILogger<AirlineDataController> _logger;
        private readonly IConfiguration _configuration;
        private readonly EnterpriseDbContext _dbContext;

        private readonly bool _useQuery;

        public AirlineDataController(ILogger<AirlineDataController> logger, IConfiguration configuration,
            EnterpriseDbContext dbContext)
        {
            _logger = logger;
            _configuration = configuration;
            _dbContext = dbContext;
            var section = _configuration.GetSection("FeatureFlags");
            {
                if (section!.Exists() && section.GetChildren().Any(item => item.Key == "UseQuery"))
                {
                    _useQuery = _configuration.GetValue<bool>("FeatureFlags:UseQuery");
                }
            }
        }

        [HttpGet("GetAirlineData")]
        public IEnumerable<Extract.ExtractAirlineData> GetAirlineData(bool isTrain = false)
        {
            _logger.LogDebug("Get airline user data");
            var result = default(IEnumerable<AirlineData>);

            return _dbContext.AirlineData.Where(r => r.IsTrain == isTrain)?.Select(Extract.ExtractAirlineData.Map).Take(5);
        }

        //[HttpPost("AddCauseCode")]
        //public ActionResult AddCauseCode(IEnumerable<Import.ImportCauseCode> causeCodes)
        //{

        //    Func<CauseCode, Import.ImportCauseCode, bool> finder = (existingItem, importItem) =>
        //    {
        //        return existingItem.CauseCodeName == importItem.CauseCodeName;
        //    };

        //    Func<Import.ImportCauseCode, CauseCode, CauseCode> transformer = (importItem, extistingItem) =>
        //    {
        //        if (extistingItem is null)
        //        {
        //            return new CauseCode
        //            {
        //                CauseCodeId = 0,
        //                CauseCodeName = importItem.CauseCodeName,
        //                CauseText = importItem.CauseText,
        //            };
        //        }
        //        else
        //        {
        //            return new CauseCode
        //            {
        //                CauseCodeId = extistingItem.CauseCodeId,
        //                CauseCodeName = importItem.CauseCodeName,
        //                CauseText = importItem.CauseText,
        //            };
        //        }
        //    };

        //    var result = EntityUtil.AddEntity(_dbContext, _dbContext.CauseCodes, causeCodes, finder, transformer, true);

        //    return result switch
        //    {
        //        Result r when r.GetType().IsAssignableFrom(typeof(Result.Ok<bool>)) => Ok(),
        //        Result r when r.GetType().IsAssignableFrom(typeof(Result.Ok<int>)) => Ok(r),
        //        Result.Error error => Ok(error),
        //        _ => throw new NotImplementedException(),
        //    };
        //}
    }
}