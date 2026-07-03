using CampusCompanion.Components;

var builder = WebApplication.CreateBuilder(args);


builder.Services.AddRazorComponents() // AddRazorComponents() - This tells the server to look out for .razor files.
                                      // It loads the tools needed to read, compile and prepare blazor page components. 

    .AddInteractiveServerComponents(); // This prepares the server to handle user interactions like button clicks and live UI updates.

var app = builder.Build();


if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
    app.UseHsts();
}
app.UseStatusCodePagesWithReExecute("/not-found", createScopeForStatusCodePages: true);
app.UseHttpsRedirection();

app.UseAntiforgery();

app.MapStaticAssets();
app.MapRazorComponents<App>() // This tells the server to look for the App.razor file and use it as the main entry point for the application.
    .AddInteractiveServerRenderMode();

app.Run();
