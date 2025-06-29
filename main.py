from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = "7aef427bb868464bda524011"  # ✅ Your API key

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "converted": None, "error": None})

@app.post("/convert", response_class=HTMLResponse)
async def convert(
    request: Request,
    from_currency: str = Form(...),
    to_currency: str = Form(...),
    amount: float = Form(...)
):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        result = r.json()
        print("API RESPONSE:", result)

        if result.get("result") != "success":
            return templates.TemplateResponse("index.html", {
                "request": request,
                "converted": None,
                "error": result.get("error-type", "Conversion failed.")
            })

        converted_amount = result["conversion_result"]
        return templates.TemplateResponse("index.html", {
            "request": request,
            "converted": converted_amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "amount": amount,
            "error": None
        })

@app.get("/convert")
async def convert_api(from_currency: str, to_currency: str, amount: float):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        result = r.json()
        print("API DEBUG (GET):", result)

        return {
            "converted_amount": result.get("conversion_result", "Conversion failed"),
            "success": result.get("result") == "success"
        }

