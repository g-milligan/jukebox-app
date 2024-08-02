set itemValue=%1
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/items?item=%itemValue%