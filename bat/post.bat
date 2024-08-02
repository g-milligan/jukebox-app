set itemValue=%1
if not defined itemValue (set itemValue="grape")
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/items?item=%itemValue%