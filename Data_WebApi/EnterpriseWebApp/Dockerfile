FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR "/code/webapp"
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /code

COPY ./EnterpriseWebApp /code/EnterpriseWebApp

RUN dotnet restore "/code/EnterpriseWebApp/EnterpriseWebApp.csproj"
COPY . .
WORKDIR "/code/EnterpriseWebApp"

RUN dotnet build "EnterpriseWebApp.csproj" -c Release -o /code/webapp/build

FROM build AS publish
RUN dotnet publish "EnterpriseWebApp.csproj" -c Release -o /code/webapp/publish


FROM base AS final
WORKDIR /app
COPY --from=publish code/webapp/publish .
ENTRYPOINT ["dotnet", "EnterpriseWebApp.dll"]
