using Newtonsoft.Json;
using EnterpriseWebApp.Models.Attributes;

namespace EnterpriseWebApp.Models.Extract
{
    public class ExtractAirlineData : IDataEntityObjects
    {
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore, PropertyName = "AirlineDataID")]
        [ModelViewColumn(DisplayName = "AirlineDataID", ToDisplay = true)]
        public int ID { get; set; }

        [JsonProperty(PropertyName = "User_id")]
        [ModelViewColumn(DisplayName = "User_id", ToDisplay = true)]
        public int User_ID { get; set; }

        [JsonProperty(PropertyName = "Gender")]
        [ModelViewColumn(DisplayName = "Gender", ToDisplay = true)]
        public string Gender { get; set; }

        [JsonProperty(PropertyName = "CustomerType")]
        [ModelViewColumn(DisplayName = "CustomerType", ToDisplay = true)]
        public string CustomerType { get; set; }

        [JsonProperty(PropertyName = "Age")]
        [ModelViewColumn(DisplayName = "Age", ToDisplay = true)]
        public int Age { get; set; }

        [JsonProperty(PropertyName = "TravelType")]
        [ModelViewColumn(DisplayName = "TravelType", ToDisplay = true)]
        public string TravelType { get; set; }

        [JsonProperty(PropertyName = "Class")]
        [ModelViewColumn(DisplayName = "Class", ToDisplay = true)]
        public string Class { get; set; }

        [JsonProperty(PropertyName = "Distance")]
        [ModelViewColumn(DisplayName = "Distance", ToDisplay = true)]
        public int Distance { get; set; }

        [JsonProperty(PropertyName = "InflightWifi")]
        [ModelViewColumn(DisplayName = "InflightWifi", ToDisplay = true)]
        public int InflightWifi { get; set; }

        [JsonProperty(PropertyName = "DeptArriveConvenience")]
        [ModelViewColumn(DisplayName = "DeptArriveConvenience", ToDisplay = true)]
        public int DeptArriveConvenience { get; set; }

        [JsonProperty(PropertyName = "OnlineBooking")]
        [ModelViewColumn(DisplayName = "OnlineBooking", ToDisplay = true)]
        public int OnlineBooking { get; set; }

        [JsonProperty(PropertyName = "GateLocation")]
        [ModelViewColumn(DisplayName = "GateLocation", ToDisplay = true)]
        public int GateLocation { get; set; }

        [JsonProperty(PropertyName = "Food")]
        [ModelViewColumn(DisplayName = "Food", ToDisplay = true)]
        public int Food { get; set; }

        [JsonProperty(PropertyName = "OnlineBoarding")]
        [ModelViewColumn(DisplayName = "OnlineBoarding", ToDisplay = true)]
        public int OnlineBoarding { get; set; }

        [JsonProperty(PropertyName = "SeatComfort")]
        [ModelViewColumn(DisplayName = "SeatComfort", ToDisplay = true)]
        public int SeatComfort { get; set; }

        [JsonProperty(PropertyName = "InflightEntertainment")]
        [ModelViewColumn(DisplayName = "InflightEntertainment", ToDisplay = true)]
        public int InflightEntertainment { get; set; }

        [JsonProperty(PropertyName = "OnboardService")]
        [ModelViewColumn(DisplayName = "OnboardService", ToDisplay = true)]
        public int OnboardService { get; set; }

        [JsonProperty(PropertyName = "LegRoom")]
        [ModelViewColumn(DisplayName = "LegRoom", ToDisplay = true)]
        public int LegRoom { get; set; }

        [JsonProperty(PropertyName = "Baggage")]
        [ModelViewColumn(DisplayName = "Baggage", ToDisplay = true)]
        public int Baggage { get; set; }

        [JsonProperty(PropertyName = "Checkin")]
        [ModelViewColumn(DisplayName = "Checkin", ToDisplay = true)]
        public int Checkin { get; set; }

        [JsonProperty(PropertyName = "InflightService")]
        [ModelViewColumn(DisplayName = "InflightService", ToDisplay = true)]
        public int InflightService { get; set; }

        [JsonProperty(PropertyName = "Cleanliness")]
        [ModelViewColumn(DisplayName = "Cleanliness", ToDisplay = true)]
        public int Cleanliness { get; set; }

        [JsonProperty(PropertyName = "DepartDelay")]
        [ModelViewColumn(DisplayName = "DepartDelay", ToDisplay = true)]
        public int DepartDelay { get; set; }

        [JsonProperty(PropertyName = "ArriveDelay")]
        [ModelViewColumn(DisplayName = "ArriveDelay", ToDisplay = true)]
        public int ArriveDelay { get; set; }

        [JsonProperty(PropertyName = "Satisfaction")]
        [ModelViewColumn(DisplayName = "Satisfaction", ToDisplay = true)]
        public string Satisfaction { get; set; }

        [JsonProperty(PropertyName = "DataDate")]
        [ModelViewColumn(DisplayName = "DataDate", ToDisplay = true)]
        public DateTime DataDate { get; set; }

        [JsonProperty(PropertyName = "IsTrain")]
        [ModelViewColumn(DisplayName = "IsTrain", ToDisplay = true)]
        public bool IsTrain { get; set; }

        public ExtractAirlineData()
        {

        }

        public ExtractAirlineData(int iD, int user_ID, string gender, string customerType, int age, string travelType, string @class, int distance, int inflightWifi,
            int deptArriveConvenience, int onlineBooking, int gateLocation, int food, int onlineBoarding, int seatComfort, int inflightEntertainment, int onboardService,
            int legRoom, int baggage, int checkin, int inflightService, int cleanliness, int departDelay, int arriveDelay, string satisfaction, DateTime dataDate, bool isTrain)
        {
            ID = iD;
            User_ID = user_ID;
            Gender = gender;
            CustomerType = customerType;
            Age = age;
            TravelType = travelType;
            Class = @class;
            Distance = distance;
            InflightWifi = inflightWifi;
            DeptArriveConvenience = deptArriveConvenience;
            OnlineBooking = onlineBooking;
            GateLocation = gateLocation;
            Food = food;
            OnlineBoarding = onlineBoarding;
            SeatComfort = seatComfort;
            InflightEntertainment = inflightEntertainment;
            OnboardService = onboardService;
            LegRoom = legRoom;
            Baggage = baggage;
            Checkin = checkin;
            InflightService = inflightService;
            Cleanliness = cleanliness;
            DepartDelay = departDelay;
            ArriveDelay = arriveDelay;
            Satisfaction = satisfaction;
            DataDate = dataDate;
            IsTrain = isTrain;
        }

        public static ExtractAirlineData Map(ETL.AirlineData item) => new ExtractAirlineData
        {
            Age = item.Age,
            ArriveDelay = item.ArriveDelay,
            Baggage = item.Baggage,
            Checkin = item.Checkin,
            Class = item.Class,
            Cleanliness = item.Cleanliness,
            CustomerType = item.CustomerType,
            DataDate = item.DataDate,
            DepartDelay = item.DepartDelay,
            DeptArriveConvenience = item.DeptArriveConvenience,
            Distance = item.Distance,
            Food = item.Food,
            GateLocation = item.GateLocation,
            Gender = item.Gender,
            ID = item.ID,
            InflightEntertainment = item.InflightEntertainment,
            InflightService = item.InflightService,
            InflightWifi = item.InflightWifi,
            IsTrain = item.IsTrain,
            LegRoom = item.LegRoom,
            OnboardService = item.OnboardService,
            OnlineBoarding = item.OnlineBoarding,
            OnlineBooking = item.OnlineBooking,
            Satisfaction = item.Satisfaction,
            SeatComfort = item.SeatComfort,
            TravelType = item.TravelType,
            User_ID = item.User_ID
        };
    }
}