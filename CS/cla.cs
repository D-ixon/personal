public class VisualNode
{
    // Field: Private data, hidden from the outside world
    private string _nodeId;

    // Property: The public way to access/set the ID
    public string NodeId 
    { 
        get { return _nodeId; }
        set { _nodeId = value; }
    }

    // Constructor: Runs when you create a new Object
    public VisualNode(string id)
    {
        _nodeId = id;
    }

    // Method: Behavior
    public void Display()
    {
        Console.WriteLine($"Node ID: {NodeId}");
    }
}