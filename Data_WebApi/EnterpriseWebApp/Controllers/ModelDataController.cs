using System.Data;
using EnterpriseWebApp.Data;
using EnterpriseWebApp.Utils;
using EnterpriseWebApp.Models;
using Microsoft.AspNetCore.Mvc;
using EnterpriseWebApp.Models.ETL;
using EnterpriseWebApp.Models.Modelling;
using Import = EnterpriseWebApp.Models.Import;
using Extract = EnterpriseWebApp.Models.Extract;

namespace EnterpriseWebApp.Controllers
{
    [ApiController]
    [Route("api/etl/[controller]")]

    public class ModelDataController : ControllerBase
    {
        private readonly ILogger<ModelDataController> _logger;
        private readonly IConfiguration _configuration;
        private readonly EnterpriseDbContext _dbContext;

        private readonly bool _useQuery;

        public ModelDataController(ILogger<ModelDataController> logger, IConfiguration configuration,
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

        [HttpGet("GetModelData")]
        public IEnumerable<Extract.ExtractCleanModelInput> GetModelData(DateTime runDate, bool isTrain)
        {
            _logger.LogDebug("Get model train data");
            var result = default(IEnumerable<Extract.ExtractCleanModelInput>);

            var max_runDate = _dbContext.ModelInputs.Select(r => r.RunDate).Max();

            runDate = runDate == default ? max_runDate : runDate;

            return _dbContext.ModelInputs?.Where(r => r.RunDate == runDate && r.IsTrain == isTrain)?.Select(Extract.ExtractCleanModelInput.Map);
        }

        [HttpPost("SaveCleanModelInput")]
        public ActionResult SaveCleanModelInput(IEnumerable<Import.ImportCleanModelInput> modelInputs, DateTime runDate, bool deleteExisting)
        {
            runDate = runDate == default ? DateTime.Now : runDate;


            if (deleteExisting)
            {
                var existingRecords = _dbContext.ModelInputs.Where(e => e.RunDate == runDate).ToList();

                if (existingRecords.Any())
                {
                    EntityUtil.RemoveEntity(_dbContext, _dbContext.ModelInputs, existingRecords);
                }
            }

            Func<CleanModelInput, Import.ImportCleanModelInput, bool> finder = (_, _) => false;


            Func<Import.ImportCleanModelInput, CleanModelInput, CleanModelInput> transformer = (importItem, existingItem) =>
            {
                if (existingItem is null)
                {
                    return new CleanModelInput
                    {
                        ID = 0,
                        Age = importItem.Age,
                        ArriveDelay = importItem.ArriveDelay,
                        Baggage = importItem.Baggage,
                        Checkin = importItem.Checkin,
                        AirlineDataID = importItem.AirlineDataID,
                        Class_Business = importItem.Class_Business,
                        CustomerType_Disloyal = importItem.CustomerType_Disloyal,
                        CustomerType_Loyal = importItem.CustomerType_Loyal,
                        Gender_Female = importItem.Gender_Female,
                        Gender_Male = importItem.Gender_Male,
                        TravelType_Business = importItem.TravelType_Business,
                        Cleanliness = importItem.Cleanliness,
                        DataDate = importItem.DataDate,
                        DepartDelay = importItem.DepartDelay,
                        DeptArriveConvenience = importItem.DeptArriveConvenience,
                        Distance = importItem.Distance,
                        Food = importItem.Food,
                        GateLocation = importItem.GateLocation,
                        InflightEntertainment = importItem.InflightEntertainment,
                        InflightService = importItem.InflightService,
                        InflightWifi = importItem.InflightWifi,
                        IsTrain = importItem.IsTrain,
                        LegRoom = importItem.LegRoom,
                        OnboardService = importItem.OnboardService,
                        OnlineBoarding = importItem.OnlineBoarding,
                        OnlineBooking = importItem.OnlineBooking,
                        Satisfaction = importItem.Satisfaction,
                        SeatComfort = importItem.SeatComfort,
                        Class_Eco = importItem.Class_Eco,
                        TravelType_Personal = importItem.TravelType_Personal,
                        //User_ID = importItem.User_ID,
                        RunDate = runDate
                    };
                }
                else
                {
                    return new CleanModelInput
                    {
                        ID = existingItem.ID,
                        Age = importItem.Age,
                        ArriveDelay = importItem.ArriveDelay,
                        Baggage = importItem.Baggage,
                        Checkin = importItem.Checkin,
                        AirlineDataID = importItem.AirlineDataID,
                        Class_Business = importItem.Class_Business,
                        CustomerType_Disloyal = importItem.CustomerType_Disloyal,
                        CustomerType_Loyal = importItem.CustomerType_Loyal,
                        Gender_Female = importItem.Gender_Female,
                        Gender_Male = importItem.Gender_Male,
                        TravelType_Business = importItem.TravelType_Business,
                        Cleanliness = importItem.Cleanliness,
                        DataDate = importItem.DataDate,
                        DepartDelay = importItem.DepartDelay,
                        DeptArriveConvenience = importItem.DeptArriveConvenience,
                        Distance = importItem.Distance,
                        Food = importItem.Food,
                        GateLocation = importItem.GateLocation,
                        InflightEntertainment = importItem.InflightEntertainment,
                        InflightService = importItem.InflightService,
                        InflightWifi = importItem.InflightWifi,
                        IsTrain = importItem.IsTrain,
                        LegRoom = importItem.LegRoom,
                        OnboardService = importItem.OnboardService,
                        OnlineBoarding = importItem.OnlineBoarding,
                        OnlineBooking = importItem.OnlineBooking,
                        Satisfaction = importItem.Satisfaction,
                        SeatComfort = importItem.SeatComfort,
                        Class_Eco = importItem.Class_Eco,
                        TravelType_Personal = importItem.TravelType_Personal,
                        //User_ID = importItem.User_ID,
                        RunDate = runDate
                    };
                }
            };

            var result = EntityUtil.AddEntity(_dbContext, _dbContext.ModelInputs, modelInputs, finder, transformer, false);

            return result switch
            {
                Result r when r.GetType().IsAssignableFrom(typeof(Result.Ok<bool>)) => Ok(),
                Result r when r.GetType().IsAssignableFrom(typeof(Result.Ok<int>)) => Ok(r),
                Result.Error error => Ok(error),
                _ => throw new NotImplementedException(),
            };
        }


        [HttpPost("SavePredictionResults")]
        public ActionResult SavePredictionResults(IEnumerable<Import.ImportPredictionResult> predictionResutls, DateTime runDate, bool deleteExisting)
        {
            runDate = runDate == default ? DateTime.Now : runDate;


            if (deleteExisting)
            {
                var existingRecords = _dbContext.Predictions.Where(e => e.RunDate == runDate).ToList();

                if (existingRecords.Any())
                {
                    EntityUtil.RemoveEntity(_dbContext, _dbContext.Predictions, existingRecords);
                }
            }

            Func<PredictionResult, Import.ImportPredictionResult, bool> finder = (_, _) => false;


            Func<Import.ImportPredictionResult, PredictionResult, PredictionResult> transformer = (importItem, existingItem) =>
            {
                if (existingItem is null)
                {
                    return new PredictionResult
                    {
                        ID = 0,
                        Data_ID = importItem.Data_ID,
                        Satisfaction = importItem.Satisfaction == "0" ? "neutral or dissatisfied": "satisfied",
                        RunDate = runDate
                    };
                }
                else
                {
                    return new PredictionResult
                    {
                        ID = existingItem.ID,
                        Data_ID = importItem.Data_ID,
                        Satisfaction = importItem.Satisfaction == "0" ? "neutral or dissatisfied" : "satisfied",
                        RunDate = runDate
                    };
                }
            };

            var result = EntityUtil.AddEntity(_dbContext, _dbContext.Predictions, predictionResutls, finder, transformer, false);

            return result switch
            {
                Result r when r.GetType().IsAssignableFrom(typeof(Result.Ok<bool>)) => Ok(),
                Result r when r.GetType().IsAssignableFrom(typeof(Result.Ok<int>)) => Ok(r),
                Result.Error error => Ok(error),
                _ => throw new NotImplementedException(),
            };
        }

    }
}
