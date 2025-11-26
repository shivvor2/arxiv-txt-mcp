import os
import requests
from fastmcp import FastMCP
from dotenv import load_dotenv

mcp = FastMCP("arxiv-txt")

load_dotenv()
ARXIV_TXT_BASE_URL = os.environ.get("ARXIV_TXT_URL", "https://arxiv-txt.org")

@mcp.tool
def get_summary(arxiv_id: str) -> str:
    """
    Fetches the summary of an arXiv paper.

    :param arxiv_id: The ID of the arXiv paper (e.g., "1706.03762").
    :return: Summary and metadata (title, authors, bibliography) of the paper as a string.
    """
    url = f"{ARXIV_TXT_BASE_URL}/raw/abs/{arxiv_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching summary: {e}"

@mcp.tool
def get_full_paper(arxiv_id: str) -> str:
    """
    Fetches the full content of an arXiv paper.

    :param arxiv_id: The ID of the arXiv paper (e.g., "1706.03762").
    :return: The full content of the paper as a string.
    """
    url = f"{ARXIV_TXT_BASE_URL}/raw/pdf/{arxiv_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching full paper: {e}"

if __name__ == "__main__":
    mcp.run()