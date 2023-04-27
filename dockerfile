FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./src/app /code/app


FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR "/code/webapp"
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /code

COPY ./Data_WebApi/EnterpriseWebApp /code/EnterpriseWebApp


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

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


