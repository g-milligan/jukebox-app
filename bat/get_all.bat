set limit=%1
if not defined limit (set limit=100)
curl http://127.0.0.1:8000/items?limit=%limit%