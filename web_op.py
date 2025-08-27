from dotenv import load_dotenv
import os
import requests
from urllib.parse import quote_plus
load_dotenv()


dataset_id="gd_lvz8ah06191smkebj4"

def make_api_request(url,**kwargs):
    api_key=os.getenv("BRIGHTDATA_API")
    headers={
        "Authorization":f"Bearer {api_key}",
        "Content-type":"application/json"
    }
    try:
        response=requests.post(url,headers=headers,**kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API req error!:{e}")
        return None
    except Exception as e:
        print("Unknown error:",e)
        return None
def serp_search(query,engine="google"):
    if engine=='google':
        base_url="https://www.google.com/search"
    elif engine=='bing':
        base_url="https://www.bing.com/search"
    else:
        raise ValueError("Unknown engine")
    url="https://api.brightdata.com/request"
    
    payload={
        "zone":"ai_agent",
        "url": f"{base_url}?q={quote_plus(query)}&brd_json=1",
        "format":"raw"
    }
    full_response=make_api_request(url,json=payload)
    
    if not full_response:
        return None
    extracted_data={
        "knowledge":full_response.get("knowledge",{}),
        "organic":full_response.get('organic',[]),
    }
    
    return extracted_data
def _trigger_and_download_snapshot(trigger_url,params,data, operation_name="operation"):
    trigger_result=make_api_request(trigger_url,params=params,json=data)
    if not trigger_result:
        return None
    snapshot_id=trigger_result.get("snapshot_id")
    if not snapshot_id:
        return None
    
def reddit_search(keyword,date="All Time",sort_by="Hot",num_of_posts=25):
    trigger_url="https://api.brightdata.com/datasets/v3/trigger"
    
    params={
        "dataset_id":"gd_lvz8ah06191smkebj4",
        "include_errors":"true",
        "type":"discover_new",
        "discover_by":"keyword",
        
    }
    data=[
        {
            "keyword":keyword,
            "date":date,
            "sort_by":sort_by,
            "num_of_posts":num_of_posts
        }
    ]
    raw_data=None
    
    if not raw_data:
        return None
    return None