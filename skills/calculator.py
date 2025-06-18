# skills/calculator.py
def solve(query):
    try:
        expression = query.replace("what is", "").strip()
        result = eval(expression)
        return f"The result is {result}"
    except:
        return "I couldn't solve that."
