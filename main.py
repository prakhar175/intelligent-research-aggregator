from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import Annotated, List
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
from web_op import serp_search
load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-20b")

class State(TypedDict):
    messages:Annotated[list,add_messages] #tell lanngraph not overwrite the message instead add it in metadata of messages
    user_question: str|None
    google_results: str| None
    bing_results: str| None
    reddit_results: str| None
    selected_reddit_url: List[str] | None
    reddit_post_data: list| None
    google_analysis: str|None
    bing_analysis: str|None
    reddit_analysis: str|None
    final_answer:str|None

def google_search(state:State):
    user_question=state.get("user_question"," ")
    print(f"Searching Google for:{user_question}")
    google_results=serp_search(user_question,engine="google")
    print(google_results)
    return {"google_results":google_results}


def bing_search(state:State):
    user_question=state.get("user_question"," ")
    print(f"Searching bing for:{user_question}")
    bing_results=serp_search(user_question,engine="bing")
    print(bing_results)
    return {"bing_results":bing_results}


def reddit_search(state:State):
    user_question=state.get("user_question"," ")
    print(f"Searching reddit for:{user_question}")
    reddit_results=[]
    return {"reddit_results":reddit_results}


def analyse_reddit_posts(state:State):
    return {"selected_reddit_urls":[]}


def retrieve_reddit_posts(state:State):
    return {"reddit_post_data":[]}


def analyze_google_results(state:State):
    return {"google_analysis":""}


def analyze_bing_results(state:State):
    return {"bing_analysis":""} 


def analyze_reddit_results(state:State):
    return {"reddit_analysis":""} 

def synthesize_analyses(state:State):
    return {"final_answer":""}

graph_builder=StateGraph(State)


graph_builder.add_node("google_search",google_search)
graph_builder.add_node("bing_search",bing_search)
graph_builder.add_node("reddit_search",reddit_search)
graph_builder.add_node("analyse_reddit_posts",analyse_reddit_posts)
graph_builder.add_node("retrieve_reddit_posts",retrieve_reddit_posts)
graph_builder.add_node("analyze_google_results",analyze_google_results)
graph_builder.add_node("analyze_bing_results",analyze_bing_results)
graph_builder.add_node("analyze_reddit_results",analyze_reddit_results)
graph_builder.add_node("synthesize_analyses",synthesize_analyses)


graph_builder.add_edge(START,"google_search")
graph_builder.add_edge(START,"bing_search")
graph_builder.add_edge(START,"reddit_search")

graph_builder.add_edge("google_search","analyse_reddit_posts")
graph_builder.add_edge("bing_search","analyse_reddit_posts")
graph_builder.add_edge("reddit_search","analyse_reddit_posts")


graph_builder.add_edge("analyse_reddit_posts","retrieve_reddit_posts")

graph_builder.add_edge("retrieve_reddit_posts","analyze_google_results")
graph_builder.add_edge("retrieve_reddit_posts","analyze_bing_results")
graph_builder.add_edge("retrieve_reddit_posts","analyze_reddit_results")

graph_builder.add_edge("analyze_google_results","synthesize_analyses")
graph_builder.add_edge("analyze_bing_results","synthesize_analyses")
graph_builder.add_edge("analyze_reddit_results","synthesize_analyses")


graph_builder.add_edge("synthesize_analyses",END)

graph=graph_builder.compile()

def run_chatbot():
    print("Multi-Source Researh Agent")
    print("Type 'exit' to EXIT\n")
    while True:
        user_input=input("Ask me a question:   ")
        if user_input.lower()=='exit':
            print("Exiting . . . ")
            break
        state={
            "messages":[{"role":"user","content":user_input}],
            "user_question":user_input,
            "google_results":  None,
            "bing_results":  None,
            "reddit_results":  None,
            "selected_reddit_url":  None,
            "reddit_post_data":  None,
            "google_analysis": None,
            "bing_analysis": None,
            "reddit_analysis": None,
            "final_answer":None
        }
        
        print("\n Starting parallel research process . . .")
        print("Launching Google, Bing, Reddit searches... \n")
        
        final_state=graph.invoke(state)
        if final_state.get("final_answer"):
            print(f"\nFinal Answer:\n {final_state.get('final_answer')}")
            
        print("-"*100)
if __name__=="__main__":
    run_chatbot()