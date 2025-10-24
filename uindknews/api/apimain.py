from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os


app = FastAPI(title='Unofficial UIN Datokarama News API', version='1.0.0')

class NewsList(BaseModel):
    url : str
    news_title : str
    author : str
    issued : str
    news_content : str

class NewsListResponse(BaseModel):
    code: int
    message: str
    count: int
    data: list[NewsList]
    
def load_json_data(file_location: str):
    print("Current working dir:", os.getcwd())
    print("File exists:", os.path.exists(file_location))
    try:
        with open(file_location, 'r', encoding='utf-8') as json_file:
            raw_data = json.load(json_file)
            return [NewsList(**data) for data in raw_data]
        
    except Exception as e:
        print(e)
        return []
    
@app.get('/api/v1')
def index():
    return {
        'status_code': 200,
        'docs': 'base_url/docs'
    }

@app.get('/api/v1/news', response_model=NewsListResponse, name='list of 9 new news')
def news_list():
    file_json_location = 'data_feed/news_data.json'
    datas = load_json_data(file_json_location)
    if not datas:
        raise HTTPException(status_code=404, detail='news not found / not update yet')
    
    return {
        'code': 200,
        'message': 'Retrieve Data Success',
        'count': len(datas),
        'data': datas,
    }
    
    