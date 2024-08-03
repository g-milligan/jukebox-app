set indexValue=%1
if not defined indexValue (set indexValue=0)
curl http://127.0.0.1:8000/item/%indexValue%