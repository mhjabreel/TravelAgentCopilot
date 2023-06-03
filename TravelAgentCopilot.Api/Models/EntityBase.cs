namespace TravelAgentCopilot.Api.Models;

public abstract class EntityBase
{
    public string Id { get; set; } = Guid.NewGuid().ToString("N");

    public DateTime CreatedAt { get; set; } = DateTime.Now;
}