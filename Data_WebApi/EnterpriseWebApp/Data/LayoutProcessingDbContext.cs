﻿using EnterpriseWebApp.Models.ETL;
using Microsoft.EntityFrameworkCore;

namespace EnterpriseWebApp.Data
{
    public class EnterpriseDbContext : DbContext
    {
        private ILogger _logger;
        private IConfiguration _configuration;

        public EnterpriseDbContext(ILogger<EnterpriseDbContext> logger, IConfiguration configuration, DbContextOptions<EnterpriseDbContext> options)
           : base(options)
        {
            this._logger = logger;
            this._configuration = configuration;
        }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer(_configuration.GetConnectionString("layoutProcessing"));
        }

        public virtual DbSet<AirlineData> AirlineData { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<AirlineData>(entity =>
            {
                entity.HasKey(e => e.ID);
                entity.ToTable("airline_raw", "dbo");

                entity.Property(e => e.User_ID).HasColumnName("User_id");
                entity.Property(e => e.Gender).HasColumnName("Gender");
                entity.Property(e => e.CustomerType).HasColumnName("CustomerType");
                entity.Property(e => e.Age).HasColumnName("Age");
                entity.Property(e => e.TravelType).HasColumnName("TravelType");
                entity.Property(e => e.Class).HasColumnName("Class");
                entity.Property(e => e.Distance).HasColumnName("Distance");
                entity.Property(e => e.InflightWifi).HasColumnName("InflightWifi");
                entity.Property(e => e.DeptArriveConvenience).HasColumnName("DeptArriveConvenience");
                entity.Property(e => e.OnlineBooking).HasColumnName("OnlineBooking");
                entity.Property(e => e.GateLocation).HasColumnName("GateLocation");
                entity.Property(e => e.Food).HasColumnName("Food");
                entity.Property(e => e.OnlineBoarding).HasColumnName("OnlineBoarding");
                entity.Property(e => e.InflightEntertainment).HasColumnName("InflightEntertainment");
                entity.Property(e => e.SeatComfort).HasColumnName("SeatComfort");
                entity.Property(e => e.LegRoom).HasColumnName("LegRoom");
                entity.Property(e => e.Baggage).HasColumnName("Baggage");
                entity.Property(e => e.Checkin).HasColumnName("Checkin");
                entity.Property(e => e.InflightService).HasColumnName("InflightService");
                entity.Property(e => e.Cleanliness).HasColumnName("Cleanliness");

                entity.Property(e => e.DepartDelay).HasColumnName("DepartDelay");

                entity.Property(e => e.ArriveDelay).HasColumnName("ArriveDelay");

                entity.Property(e => e.DataDate).HasColumnName("DataDate");
                entity.Property(e => e.Satisfaction).HasColumnName("Satisfaction");
                entity.Property(e => e.IsTrain).HasColumnName("IsTrain").HasConversion<int>();

            });
        }
    }
}