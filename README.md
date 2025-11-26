# arXiv-txt MCP Server

An MCP server for [arxiv-txt.org](https://arxiv-txt.org), providing LLM-friendly plain text summaries and full content of arXiv papers rendered from source TeX.

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![X (formerly Twitter) URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Fx.com%2FshivVor2&style=social)


## Features

-   **Paper Summary**: Retrieve the plain text abstract of any arXiv paper.
-   **Full Paper Content**: Fetch the entire content of a paper in plain text format.
-   **Self-Host Support**: Can be configured to point to a self-hosted `arxiv-txt` instance via an environment variable.

### Tools

-   `get_summary(arxiv_id: str) -> str`
    Fetches the summary of a paper given its arXiv ID (e.g., "1706.03762").

-   `get_full_paper(arxiv_id: str) -> str`
    Fetches the full paper content for a given arXiv ID.

## Installation and Usage

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Ensure `requirements.txt` includes `fastmcp`, `requests`, and `python-dotenv`)*

3.  **(Optional) Configure for a self-hosted instance:**
    Create a `.env` file in the root directory to specify a custom `arxiv-txt` URL:
    ```
    ARXIV_TXT_URL=http://localhost:8000
    ```

4.  **Run the server locally:**
    ```bash
    python arxiv_txt_server.py
    ```

5.  **Connect from an MCP Client:**
    For clients that support it, add a server entry to your configuration file:
    ```json
    "mcpServers": {
      "arxiv-txt": {
        "command": "python",
        "args": [
          "/path/to/your/main.py"
        ]
      }
    }
    ```

## Examples

After installation, you can ask your LLM assistant:

-   "What is the summary of arXiv paper 1706.03762?"
-   "Fetch the full text for the paper 'Attention is All You Need' (1706.03762)."

The client will automatically call the appropriate tools and use the content in its response.

## Why This Server?

Suits my use scenario (librechat on cloud vps) better, I prebake my mcp servers into LibreChat's `api` image.

Most arXiv MCP servers rely on local OCR libraries like `PyMuPDF`, causing:

1.  **Build Failures on Alpine Linux**: `PyMuPDF` lacks pre-built wheels for Alpine's musl libc, forcing slow source compilation that often fails during `docker build`.
2.  **Poor Accuracy & Heavy Resources**: Local OCR is resource-intensive and produces lower-quality text extraction.

Both issues are solved by delegating parsing to `arxiv-txt.org`:

-   **Lightweight**: No OCR dependencies, just `requests` and `fastmcp`.
-   **Zero Build Issues**: Works seamlessly on any OS, including Alpine Linux.
-   **Better Quality**: Uses a service optimized for clean, LLM-friendly arXiv text extraction.

Ideal for low resources environments (e.g. VPS deployments) or if `glibc` is not availiable

## License

This project is licensed under the MIT License.

## Acknowledgments

-   Built with [FastMCP](https://github.com/jlowin/fastmcp).
-   Text content provided by the [arXiv-txt.org](https://arxiv-txt.org) service.
-   This project is licensed under the MIT License.