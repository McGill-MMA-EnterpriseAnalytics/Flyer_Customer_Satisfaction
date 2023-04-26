using System.Data;
using EnterpriseWebApp.Data;
using Microsoft.AspNetCore.Mvc;
using EnterpriseWebApp.Models.ETL;
using Import = EnterpriseWebApp.Models.Import;
using Extract = EnterpriseWebApp.Models.Extract;

namespace EnterpriseWebApp.Controllers
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

    }
}