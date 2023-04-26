using EnterpriseWebApp.Models;
using Microsoft.EntityFrameworkCore;

namespace EnterpriseWebApp.Utils
{
    public static class EntityUtil
    {
        public static Result AddEntity<T, U>(DbContext dbContext, DbSet<T> dataEntity, IEnumerable<U> entities, Func<T, U, bool> finder, Func<U, T, T> transformer, bool doSearch = false) where T : class
        {
            foreach (var entity in entities.Where(entity => entity is not null))
            {
                if (doSearch && finder != null && dataEntity.AsEnumerable().Any(i => finder(i, entity)))
                {
                    var currentItem = dataEntity.AsEnumerable().FirstOrDefault(i => finder(i, entity));
                    var item = transformer(entity, currentItem);

                    if (currentItem != null && item != null)
                    {
                        dataEntity.Entry(currentItem).CurrentValues.SetValues(item);
                    }
                    else if (currentItem is null && item is not null)
                    {
                        dataEntity.Add(item);
                    }
                }
                else
                {
                    var item = transformer(entity, null);
                    dataEntity.Add(item);
                }
            }
            return new Result.Ok<int>(dbContext.SaveChanges());
        }
        public static Result RemoveEntity<T>(DbContext dbContext, DbSet<T> dataEntity, IEnumerable<T> entities) where T : class
        {
            foreach (var entity in entities.Where(entity => entity is not null))
            {
                if (dataEntity.Contains(entity))
                    dataEntity.Remove(entity);
            }
            return new Result.Ok<int>(dbContext.SaveChanges());
        }
    }
}
