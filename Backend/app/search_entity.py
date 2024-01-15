import requests
import redis
import datetime


r = redis.Redis('almogf-cache-1',6379,0)

class SearchEntity():
    word = "Test"
    times = 3
    
    def __init__(self,word,times) -> None:
        self.word = word
        self.times = times
        
      
    def search_word(self):
        entity = []
        cache_data = []
        
        if r.exists(f"{self.word}-{self.times}-1") == 0:
            print("API")
            url = "https://www.wikidata.org/w/api.php"

            query = self.word

            params = {
                "action" : "wbsearchentities",
                "language" : "en",
                "format" : "json",
                "search" : query
            }
            
            data = requests.get(url,params)
            
            
            entity.append(self.word + ',')
            cache_data.append(self.word + ',')
            
            if len(data.json()["search"]) + 1 < self.times:
                results = len(data.json()["search"]) - 1
            else:
                results = self.times
            
            for i in range(results):             
                entity.append(data.json()["search"][i+1]["display"]["description"]["value"].replace(',',''))
                cache_data.append(data.json()["search"][i+1]["display"]["description"]["value"].replace(',','') + ',')
            r.setex(
                f"{self.word}-{self.times}-1",
                datetime.timedelta(minutes=2),
                value=''.join(cache_data)
            )  
            
        else:
            print("Cache")
            entity.append(self.word)
            vals = (r.get(f"{self.word}-{self.times}-1")).decode()
            vals = vals.split(',')
            vals.pop(0)
            del vals[-1]
            for val in vals:
                entity.append(val)
            
        return {"data": entity}
        
    def search_pic(self):
        entity = []
        cache_data = []
        if r.exists(f"{self.word}-{self.times}-2") == 0:
            print("API")
            url = f"https://pixabay.com/api/?key=32362581-92d1cfd1c5aeaf195c5047a52&q={self.word}&image_type=photo&pretty=true"
            req = requests.get(url)
            entity.append(self.word)
            cache_data.append(self.word +',')
            json_data = req.json()
            for i in range(self.times):
                entity.append(json_data['hits'][i]["webformatURL"])
                cache_data.append(json_data['hits'][i]["webformatURL"] + ',')
            
            r.setex(
                f"{self.word}-{self.times}-2",
                datetime.timedelta(minutes=2),
                value=''.join(cache_data)
            )
        else:
            print("Cache")
            entity.append(self.word)
            vals = (r.get(f"{self.word}-{self.times}-2")).decode()
            vals = vals.split(',')
            vals.pop(0)
            del vals[-1]
            for val in vals:
                entity.append(val)
                
        return {"data": entity}
    
    def search_videos(self):
        entity = []
        cache_data = []
        if r.exists(f"{self.word}-{self.times}-3") == 0:
            print("API")
            API_KEY = "AIzaSyD6P931L2AmXF10WH6kKabqS63NBfz5Q8k"
            url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&q={self.word}&type=video&part=snippet&maxResults={self.times}"
            response = requests.get(url).json()
            entity.append(self.word)
            cache_data.append(self.word +',')
            snippets = response['items']
            for snippet in snippets:
                suffix = snippet['id']['videoId']
                link = f'https://www.youtube.com/watch?v={suffix}'
                entity.append(link)
                cache_data.append(link + ',')
            
            r.setex(
                f"{self.word}-{self.times}-3",
                datetime.timedelta(minutes=2),
                value=''.join(cache_data)
            )
                
        else:
            print("Cache")
            entity.append(self.word)
            vals = (r.get(f"{self.word}-{self.times}-3")).decode()
            vals = vals.split(',')
            vals.pop(0)
            del vals[-1]
            for val in vals:
                entity.append(val)
                
        return {"data": entity}
    def clear_cache(self):
        r.flushall()
        
    
    
        


    