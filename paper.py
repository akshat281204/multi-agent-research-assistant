# --- arxiv_agent_extension.py ---
from dotenv import load_dotenv
load_dotenv()
from crewai import Agent, Task, Crew
from langchain_community.llms.ollama import Ollama
import requests
from fpdf import FPDF
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# --- LLM Setup ---
llm = Ollama(
    model="ollama/mistral",
    base_url="http://localhost:11434"
)

# --- Util ---
def fetch_arxiv_papers(query):
    print("\n Searching arXiv for related research papers...")
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5"
    response = requests.get(url)
    entries = []
    if response.status_code == 200:
        from xml.etree import ElementTree
        root = ElementTree.fromstring(response.content)
        for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
            title = entry.find("{http://www.w3.org/2005/Atom}title").text.strip()
            link = entry.find("{http://www.w3.org/2005/Atom}id").text.strip()
            entries.append((title, link))
    return entries

def create_agent(role, topic):
    return Agent(
        role=role,
        goal=f"Analyze arXiv research paper trends for: {topic}",
        backstory=f"You are an insightful {role} specialized in reviewing academic research.",
        verbose=False,
        llm=llm
    )


def display_paper_list(papers):
    print("\n🔗 Top arXiv Papers:")
    for i, (title, link) in enumerate(papers, 1):
        print(f"{i}. {title}\n   {link}")

# --- Main Function ---
def main():
    topic = input("Enter a research topic: ").strip()
    if not topic:
        print("No topic provided.")
        return

    papers = fetch_arxiv_papers(topic)
    if not papers:
        print("No papers found on arXiv.")
        return

    display_paper_list(papers)

    researcher = create_agent("ArXiv Analyst", topic)
    task = Task(
        description=f"Review the following arXiv papers on '{topic}' and summarize key insights in bullet points.\n\n" +
                    "\n".join([f"{i+1}. {title}\n{link}" for i, (title, link) in enumerate(papers)]),
        agent=researcher,
        expected_output="• Bullet-point summary of insights from the arXiv papers."
    )

    crew = Crew(tasks=[task], verbose=False)
    result = crew.kickoff()

if __name__ == "__main__":
    main()