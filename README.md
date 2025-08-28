# Multi-Source Research Agent 🔍

A powerful AI-powered research Agent that aggregates information from multiple sources (Google, Bing, and Reddit) to provide comprehensive, well-rounded answers to your questions.

## 🌟 Features

- **Multi-Source Search**: Simultaneously searches Google, Bing, and Reddit for comprehensive coverage
- **Intelligent Reddit Analysis**: Analyzes Reddit posts and retrieves detailed comments from the most relevant discussions
- **Parallel Processing**: Uses LangGraph to execute searches in parallel for faster results
- **AI-Powered Analysis**: Each source is analyzed separately by AI to extract key insights
- **Smart Synthesis**: Combines all analyses into a coherent, comprehensive final answer
- **Interactive Chat Interface**: Simple command-line interface for asking questions

## 🏗️ Architecture

The system uses a **LangGraph state machine** with the following workflow:

```
Start → [Google Search, Bing Search, Reddit Search] (Parallel)
  ↓
Reddit URL Analysis (selects best Reddit posts)
  ↓
Reddit Post Retrieval (gets detailed comments)
  ↓
[Google Analysis, Bing Analysis, Reddit Analysis] (Parallel)
  ↓
Final Synthesis → End
```

## 🛠️ Tech Stack

- **LangGraph**: State machine orchestration
- **LangChain**: LLM integration and prompt management
- **Ollama**: Local LLM (Mistral) for analysis
- **BrightData API**: Web scraping for search results
- **Pydantic**: Data validation and structured outputs
- **Python 3.10+**: Core language

## 📋 Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.ai/) installed with Mistral model
- BrightData API account and API key

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-agent-langgraph
   ```

2. **Install dependencies**
   ```bash
   uv sync .
   ```

3. **Set up Ollama**
   ```bash
   # Install Ollama from https://ollama.ai/
   # Pull the Mistral model
   ollama pull mistral:latest
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   BRIGHTDATA_API=your_brightdata_api_key_here
   ```

## 💡 Usage

### Command Line Interface

Run the interactive chatbot:

```bash
uv run python main.py
```

Then ask any question:
```
Ask me a question: What are the best practices for Python web development?
```

## 🔧 Configuration

### Customizing Search Parameters

Edit `web_op.py` to modify search behavior:

```python
# Reddit search parameters
def reddit_search_api(
    keyword, 
    date="All time",        # Time range for search
    sort_by="Hot",          # Sorting method
    num_of_posts=25         # Number of posts to analyze
):
```

### Changing the LLM Model

Modify `main.py` to use different models:

```python
# Use different Ollama models
llm = ChatOllama(model="llama2:latest")  # or "codellama:latest", etc.

# Or use other LangChain-compatible LLMs
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model="gpt-4")
```

## 📁 Project Structure

```
ai-agent-langgraph/
├── main.py              # Main application and LangGraph workflow
├── prompts.py           # AI prompt templates for different analysis tasks
├── web_op.py            # Web scraping and search functionality
├── snapshot_op.py       # BrightData snapshot handling utilities
├── pyproject.toml       # Project dependencies and metadata
├── .env                 # Environment variables (create this)
└── README.md            # This file
```

## 🔍 How It Works

1. **Parallel Search Phase**: The system simultaneously searches Google, Bing, and Reddit for your question
2. **Reddit Post Selection**: AI analyzes Reddit results to select the most valuable posts for deeper analysis
3. **Content Retrieval**: Detailed comments are retrieved from selected Reddit posts
4. **Individual Analysis**: Each source (Google, Bing, Reddit) is analyzed separately to extract key insights
5. **Synthesis**: All analyses are combined into a comprehensive, well-structured final answer

## 🎯 Example Output

```
Question: "What are the pros and cons of remote work?"

Final Answer:
Based on comprehensive research across multiple sources:

**From Official Sources (Google/Bing):**
- Increased productivity and flexibility reported by 65% of companies
- Cost savings of $11,000 per employee annually on average
- Challenges with collaboration and company culture

**From Community Discussions (Reddit):**
- Users report better work-life balance but struggle with isolation
- "Working from home saved my sanity during commute hours" - r/jobs
- Mixed experiences with career advancement opportunities

**Synthesis:**
Remote work offers significant benefits in flexibility and cost savings, but requires 
careful management of communication and culture challenges...
```

## 🐛 Troubleshooting

### Common Issues

**BrightData API Errors**
- Verify your API key in the `.env` file
- Check your BrightData account credits and permissions

**Ollama Connection Issues**
- Ensure Ollama is running: `ollama serve`
- Verify Mistral model is installed: `ollama list`

**Reddit Data Retrieval Fails**
- Some Reddit URLs may be inaccessible or deleted
- The system gracefully handles missing data

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Project Link: [https://github.com/yourusername/ai-agent-langgraph](https://github.com/yourusername/ai-agent-langgraph)
