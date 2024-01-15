from fastapi import FastAPI
from pydantic import BaseModel
from app.search_entity import SearchEntity




class Search(BaseModel):
    
    summaries:list
    
    
   
app = FastAPI()


@app.get("/api/v1/")
def hello_get():
    return {"data": "Welcome to my search engine, this is the response for the basic Get request"}

@app.post("/api/v1/")
def hello_get():
    return {"data":"Welcome to my search engine, this is the response for the basic Post request"}

@app.get("/api/v1/search/{word}/times/{times}")
def search_word(word:str, times:int):
    search_ent = SearchEntity(word.lower(),times)
    return search_ent.search_word()
    
@app.post("/api/v1/clearCache")
def clearCache():
    search_ent = SearchEntity("test",1)
    search_ent.clear_cache()
    return "Cache is cleared now."

@app.get("/api/v1/photos/{photo}/times/{times}")
def search_pic(photo:str,times:int):
    search_ent = SearchEntity(photo.lower(),times)
    return search_ent.search_pic()

@app.get("/api/v1/videos/{video}/times/{times}")
def search_videos(video:str,times:int):
    search_ent = SearchEntity(video.lower(),times)
    return search_ent.search_videos()



    
    
