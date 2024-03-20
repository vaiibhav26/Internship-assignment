from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Endpoint to handle file upload
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join("uploads", filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "File uploaded successfully"}

# Endpoint to handle user query
@app.post("/predict")
async def predict(query: str):
    # Your logic to process the query and provide meaningful response
    # For simplicity, returning the query as response
    return {"response": query}

# Exception handler for unsupported file types
@app.exception_handler(HTTPException)
async def validation_exception_handler(request, exc):
    if exc.status_code == 422:
        return JSONResponse(status_code=422, content={"message": "Unsupported file type"})
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
