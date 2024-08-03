set itemValue=%1
set itemIsDone=%2
if not defined itemValue (set itemValue=grape)
if not defined itemIsDone (set itemIsDone=false)
curl -X POST -H "Content-Type: application/json" -d "[{\"text\":\"%itemValue%\",\"is_done\":%itemIsDone%}]" http://127.0.0.1:8000/items