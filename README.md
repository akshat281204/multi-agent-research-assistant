# Multi-Agent Research Assistant

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![CrewAI](https://img.shields.io/badge/CrewAI-Powered-orange?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyQzIgMTcuNTIgNi40OCAyMiAxMiAyMkMxNy41MiAyMiAyMiAxNy41MiAyMiAxMkMyMiA2LjQ4IDE3LjUyIDIgMTIgMlpNNyAxN0M2LjQ1IDE3IDYgMTYuNTUgNiAxNkM2IDE1LjQ1IDYuNDUgMTUgNyAxNUM3LjU1IDE1IDggMTUuNDUgOCAxNkM4IDE2LjU1IDcuNTUgMTcgNyAxN1pNMTcgMTdDMTYuNDUgMTcgMTYgMTYuNTUgMTYgMTZDMTYgMTUuNDUgMTYuNDUgMTUgMTcgMTVCMTcuNTUgMTUgMTggMTUuNDUgMTggMTZDMTE4IDE2LjU1IDE3LjU1IDE3IDE3IDE3Wk0xMiA3QzkuNDQgNyA3LjM3IDguNjIgNi43NSAxMS41Mkw1LjMgMTAuODJDNjIyIDcuNjMgOS4xOSA1IDEyIDVDMTQuODIgNSA2LjgzIDcuNjIgMTguNzkgMTAuODJMMTcuMjUgMTEuNTJDMTYuNjMgOC42MiAxNC41NiA3IDEyIDdaTTExIDEzQzExIDExLjkgMTEuOSA5IDEyIDlDMTIuMSAxMiAxMiAxMS45IDEzIDEzQzEzIDEzIDExIDEzIDExIDEzWiIgZmlsbD0iYmxhY2siLz4KPC9zdmc+Cg==)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-success?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MCA1MCIgd2lkdGg9IjI1IiBoZWlnaHQ9IjI1Ij48cGF0aCBkPSJNMjUgMi41Yy01LjUwNyAwLTEwIDQuNDkzLTEwIDEwVjIzSDcuNXYxLjQ4Yy0yLjAyNiAxLjE0LTMuNSAzLjMyLTMuNSA1LjUyIDAgNC4xNDIgMy4zNTggNy41IDcuNSA3LjVoMzBjNC4xNDIgMCA3LjUtMy4zNTggNy41LTcuNSAwLTIuMi0xLjQ3NC00LjM4LTMuNS01LjUydi0xLjQ4aC03LjVWMTAuNWMwLTUuNTA3LTQuNDkzLTEwLTEwLTExLjV6TTI1IDRhOC41IDguNSAwIDAxOCA4LjVWMjNoLTE2VjExLjVhOC41ID4wMSAwIDExIDk2em0tNSAxN2gxMHYuOTRoLTUuMDI3Yy0uOTc0LS4yMy0xLjk2OC0uMzA0LTMuMDM3LS4xOTMtLjg0LjA3My0xLjk2LjIxNi0xLjkzNiAxLjI1LS4wMjcuNzI2LjcyLjgyLjY0LjYyLjE3LS4xMjYgMS40NDItLjQ5NCA0LjMyOC0uNDI3LS4yMTgtLjkxNy0uNDUtMS45MjUtLjY4OC0yLjUyem0tMS41IDQuOTg2Yy01LjExIDAtOS4yNSAzLjY0LTkuMjUgOC4xNCAwIDMuMjggMi4xMjUgNi4yIDUuMjUgNy41NjV2LjgxOWgtNi45NTdjLS41NSAwLS45OTMuNDUt.OTkzIDF2NC45OTljMCAuNTUuNDQzIDEgLjk5MyAxaDEuNXYyLjY0NmwtMi41LS41di4zOTJoNWwtMi41LjUuMDQ5LS4zOThoMjZsMi40NTEuMzE1LTIuOTUxLS4zOThoLTMuNTQ5di0yLjY0NmgxLjVjLjU1IDAgLjk5My0uNDUuOTkzLTF2LTQuOTk5YzAtLjU1LS40NDMtMS0uOTkzLTFoLTYuOTU3di0uODE5YzMuMTE2LTEuMzg4IDUuMjUtNC4zMDcgNS4yNS03LjU2NSAwLTQuNS00LjE0LTguMTQtOS4yNS04LjE0eiIvPjwvc3ZnPg==)
![SerpAPI](https://img.shields.io/badge/SerpAPI-Search-blueviolet?logo=search)
![ArXiv](https://img.shields.io/badge/ArXiv-Papers-red?logo=arxiv)

This repository hosts a powerful multi-agent research assistant designed to automate the process of gathering, summarizing, and evaluating information on a given topic. Leveraging CrewAI for agent orchestration, Ollama for local LLM inference, and external APIs like SerpAPI and arXiv, this tool streamlines the initial stages of research, providing concise summaries and relevant sources.

## Table of Contents

-   [Project Description](#project-description)
-   [Features](#features)
-   [Project Structure](#project-structure)
-   [Dependencies](#dependencies)
-   [Installation](#installation)
-   [Configuration](#configuration)
-   [Usage](#usage)
-   [API Documentation](#api-documentation)
-   [Contributing](#contributing)
-   [License](#license)

## Project Description

The `multi-agent-research-assistant` project is built around a CrewAI framework, enabling a team of specialized AI agents to collaborate on research tasks. The primary goal is to take a user-defined research topic, break it down into subtopics, search for information online, summarize key findings, and even evaluate source credibility. An optional extension allows for searching and summarizing academic papers from arXiv.

This system is ideal for quickly gaining an overview of a new topic, identifying key areas of interest, and consolidating information from multiple sources.

## Features

*   **Multi-Agent Architecture**: Utilizes CrewAI to create a collaborative team of agents (Topic Analyzer, Searcher, Researcher, Summarizer, Evaluator, ArXiv Analyst).
*   **Dynamic Topic Breakdown**: Agents can analyze the main topic and suggest meaningful subtopics, or users can provide their own.
*   **Web Search Integration**: Uses SerpAPI to perform Google searches and retrieve relevant links for subtopics.
*   **Research Summarization**: Agents extract and summarize key findings into concise bullet points and a cohesive overall summary.
*   **Source Credibility Evaluation**: An agent evaluates the credibility of provided URLs, offering a score from 1-5.
*   **Local LLM Support**: Integrates with Ollama, allowing you to run powerful language models like Mistral locally without relying on external cloud services.
*   **Markdown Output**: Research outputs for each subtopic are saved as clean Markdown files.
*   **Optional arXiv Paper Search**: An extension to search for and summarize relevant academic papers from arXiv.

## Project Structure

```
.
├── .gitignore
├── main.py
├── paper.py
├── requirements.txt
└── __pycache__/
    ├── paper.cpython-311.pyc
    └── test.cpython-311.pyc
```

*   `main.py`: The core script that orchestrates the multi-agent research process, including topic analysis, web search, summarization, and evaluation.
*   `paper.py`: An optional extension script dedicated to searching and summarizing academic papers from arXiv based on a given topic.
*   `requirements.txt`: Lists all Python dependencies required to run the project.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
*   `__pycache__/`: Directory for Python bytecode cache.

## Dependencies

The project relies on the following key Python libraries:

*   `crewai`: For defining and orchestrating the multi-agent system.
*   `python-dotenv`: To load environment variables from a `.env` file.
*   `langchain-community`: Provides the interface for local LLMs like Ollama.
*   `serpapi`: For interacting with the SerpAPI Google Search API.
*   `requests`: For making HTTP requests (used in `paper.py` for arXiv API).
*   `fpdf`: A library for PDF generation (imported in `paper.py` but not currently used in the provided code).

These dependencies are listed in `requirements.txt`.

## Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/akshat281204/multi-agent-research-assistant.git
cd multi-agent-research-assistant
```

### 2. Set up a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` should contain:
```
crewai
python-dotenv
langchain-community
serpapi
requests
fpdf
```

### 4. Install and Configure Ollama

This project uses Ollama to run large language models locally.

*   **Download Ollama**: Visit [ollama.ai](https://ollama.ai/) and follow the instructions to download and install Ollama for your operating system.
*   **Download the Mistral Model**: Once Ollama is installed, open your terminal and download the `mistral` model:
    ```bash
    ollama run mistral
    ```
    This command will download the model if it's not already present and start it. You can then stop it and the model will be available for the script.

### 5. Obtain a SerpAPI API Key

This project uses SerpAPI for performing Google searches.

*   **Sign Up for SerpAPI**: Go to [serpapi.com](https://serpapi.com/) and sign up for an account. You should get a free API key.
*   **Set Environment Variable**: Create a `.env` file in the root directory of the project and add your SerpAPI key:

    ```dotenv
    SERPAPI_API_KEY="YOUR_SERPAPI_API_KEY"
    ```
    Replace `"YOUR_SERPAPI_API_KEY"` with your actual key.

## Configuration

The LLM is configured in both `main.py` and `paper.py` to use `Ollama` with the `mistral` model, assuming it's running locally on `http://localhost:11434`.

```python
llm = Ollama(
    model="ollama/mistral",
    base_url="http://localhost:11434"
)
```

Ensure your Ollama server is running and the `mistral` model is available. If you're using a different local Ollama model or a different base URL, update these lines in both `main.py` and `paper.py`.

## Usage

### Running the Main Research Assistant

To start the main research process, run `main.py`:

```bash
python main.py
```

The script will prompt you for:

1.  **Main research topic**: Enter the broad subject you want to research.
2.  **Subtopics (optional)**: You can provide specific subtopics one by one. Leave a blank line to finish. If no subtopics are provided, the system will use defaults like "Background", "Recent Advances", and "Challenges".

**Example Interaction:**

```
 Enter the main research topic: Large Language Models in Healthcare
 Enter subtopics (one per line). Leave blank line to finish:
> Applications
> Ethical Considerations
> Future Trends
>
```

The agents will then commence their tasks:
*   The `Topic Analyzer` will refine the subtopics.
*   `Searcher` agents will fetch links for each subtopic via SerpAPI.
*   `Researcher` agents will summarize findings from the links.
*   The `Summarizer` will combine all subtopic research into a cohesive summary.
*   The `Evaluator` will rate the credibility of sources.

You will see verbose output in your terminal as the agents work. Upon completion, Markdown files will be generated in your project directory, each containing the research output for a specific subtopic (e.g., `Applications_research_output.md`).

### Running the Optional arXiv Paper Search

After the main research, `main.py` will ask if you'd like to search for related arXiv papers.

```
 Would you like to also search for related arXiv papers? (y/n): y
```

If you enter `y`, `main.py` will execute `paper.py`. The `paper.py` script will automatically use the main topic you provided to `main.py` for its arXiv search.

Alternatively, you can run `paper.py` independently:

```bash
python paper.py
```

It will then prompt you to enter a research topic specifically for the arXiv search.

**Example Interaction for `paper.py` (if run standalone):**

```
Enter a research topic: Large Language Models and Drug Discovery

 Searching arXiv for related research papers...

🔗 Top arXiv Papers:
1. Large Language Models in Drug Discovery: A Comprehensive Review
   https://arxiv.org/abs/2309.0XXXX
2. ...

```

The ArXiv Analyst agent will then summarize the key insights from the found papers.

## API Documentation

This project integrates with the following external APIs:

*   **SerpAPI (Google Search API)**:
    *   Used by `main.py` to perform real-time Google searches for research subtopics.
    *   Authentication is via `SERPAPI_API_KEY` environment variable.
    *   For more details, refer to the [SerpAPI Documentation](https://serpapi.com/search-api).

*   **arXiv API**:
    *   Used by `paper.py` to search for academic papers on arXiv.
    *   Does not require an API key for basic search queries.
    *   For more details, refer to the [arXiv API User Manual](https://arxiv.org/help/api/user-manual).

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'feat: Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

Please ensure your code adheres to good practices and includes appropriate tests where applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (assuming a LICENSE file will be added).
