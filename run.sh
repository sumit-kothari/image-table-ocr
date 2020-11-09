kill -9 `lsof -t -i:8182`

nohup uvicorn main:app --host "0.0.0.0" --port 8182 &
