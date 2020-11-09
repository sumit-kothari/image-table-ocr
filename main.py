from fastapi import FastAPI, File, UploadFile
from table_ocr.demo import main as extract_table_ocr


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/uploadfile/")
def create_upload_file(file: bytes = File(...)):
    response = extract_table_ocr(file)

    print(response)
    return { "csv_data": response }