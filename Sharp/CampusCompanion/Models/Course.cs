namespace CampusCompanion.Models; // Note: This namespace must match your project name

public class Course
{
    public string Code { get; set; } = string.Empty;
    public string Title { get; set; } = string.Empty;
    public int Credits { get; set; }

    public Course(string code, string title, int credits)
    {
        Code = code;
        Title = title;
        Credits = credits;
    }
}