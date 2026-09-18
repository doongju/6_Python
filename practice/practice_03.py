import requests
 
from config import BASE, TIMEOUT, HEADERS
from parsers import parse_stocks
 
ssr = requests.get(f"{BASE}/stocks?sector=S08&market=&q=", headers=HEADERS, timeout=TIMEOUT)
 
items = parse_stocks(ssr.text)
 
print(f"{'코드':<8}{'종목명':<14}{'섹터':<10}{'현재가':>14}")
print("="*60)
for data in items:
    price_str = f"{data['price']:,}" 
    print(f"{data['code']:<8}{data['name']:<14}{data['sector']:<10}{price_str:>14}")
print("="*60)