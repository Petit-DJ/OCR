from fastapi import APIRouter, File, UploadFile
import shutil

router = APIRouter (
    prefix='/file',
    tags=['file']
)

@router.post('/files')
def get_file (file: UploadFile = File(...)):
    path = f"files/{file.filename}"
    with  open(path, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return{
        'filename': path,
        'type': file.content_type
    }