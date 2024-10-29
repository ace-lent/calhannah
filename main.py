from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def calculator_form():
    # HTML form embedded in the response
    html_content = """
    <html>
        <head>
            <title>Simple Calculator</title>
        </head>
        <body>
            <h2>Calculator</h2>
            <form action="/calculate" method="post">
                <label for="a">First Number:</label>
                <input type="number" step="any" name="a" required><br><br>
                
                <label for="b">Second Number:</label>
                <input type="number" step="any" name="b" required><br><br>
                
                <label for="operation">Operation:</label>
                <select name="operation">
                    <option value="add">Add</option>
                    <option value="subtract">Subtract</option>
                    <option value="multiply">Multiply</option>
                    <option value="divide">Divide</option>
                </select><br><br>
                
                <button type="submit">Calculate</button>
            </form>
            {% if result is not none %}
                <h3>Result: {{ result }}</h3>
            {% endif %}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(a: float = Form(...), b: float = Form(...), operation: str = Form(...)):
    # Performs the calculation based on the operation
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    # Embedding the result in the HTML content
    html_content = f"""
    <html>
        <head>
            <title>Simple Calculator</title>
        </head>
        <body>
            <h2>Calculator</h2>
            <form action="/calculate" method="post">
                <label for="a">First Number:</label>
                <input type="number" step="any" name="a" value="{a}" required><br><br>
                
                <label for="b">Second Number:</label>
                <input type="number" step="any" name="b" value="{b}" required><br><br>
                
                <label for="operation">Operation:</label>
                <select name="operation">
                    <option value="add" {"selected" if operation == "add" else ""}>Add</option>
                    <option value="subtract" {"selected" if operation == "subtract" else ""}>Subtract</option>
                    <option value="multiply" {"selected" if operation == "multiply" else ""}>Multiply</option>
                    <option value="divide" {"selected" if operation == "divide" else ""}>Divide</option>
                </select><br><br>
                
                <button type="submit">Calculate</button>
            </form>
            <h3>Result: {result}</h3>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
