# HTTP Web Proxy Server with Blacklist URL Filter

## Overview
This project implements a basic HTTP web proxy server with the following functionalities:
1. **Caching**: The proxy caches web pages for future requests to improve performance.
2. **Blacklist URL Filter**: A filter blocks specific URLs based on a local database.
3. **Error Handling**: The proxy handles errors, such as "404 Not Found" responses from web servers.

The proxy server processes simple `GET` requests and is capable of handling different types of content, such as HTML pages and images. When a client requests a webpage, the request is passed through the proxy server, which either retrieves the cached version or forwards the request to the web server. The proxy can also block specific URLs by returning an error page.

## Features
- **Caching**: 
  - Caches web pages locally on the disk.
  - Retrieves pages from the cache for subsequent requests, reducing load times.
  
- **Blacklist URL Filtering**:
  - Blocks requests to specific URLs listed in a local text file (`URL_BLOCKED.txt`).
  
- **Error Handling**:
  - Manages errors like "404 Not Found" when objects requested by the client are unavailable.
  - Displays an error page for blocked URLs and 404 errors.

## Installation
### Prerequisites
- Python 3.x
- Required Python modules:
  - `socket`
  - `requests`
  - `sys`
  - `os`

### Steps
1. Clone the repository to your local machine:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2. Install required Python modules if necessary:
    ```bash
    pip install requests
    ```
3. Create the necessary text files for blacklist and error messages:
   - `URL_BLOCKED.txt`: Add URLs (one per line) that you want to block.
   - `Error.txt`: A custom error message for a 404 Not Found error.
   - `Blocked.txt`: A custom error message for blocked URLs.

## Running the Proxy Server
1. Start the proxy server:
    ```bash
    python ProxyServer.py <server_ip>
    ```
    Example:
    ```bash
    python ProxyServer.py localhost
    ```

2. Configure your web browser to use the proxy server.  
   - For example, if the proxy is running on `localhost` at port `8888`, configure your browser to use:
     - IP Address: `localhost`
     - Port: `8888`

3. To test the proxy, visit any website using your browser (e.g., `http://www.google.com`).

## How It Works
1. **Client Request**: The client sends a `GET` request for a URL via the proxy server.
2. **Proxy Processing**:
   - **Cache Check**: If the requested page is in the cache, it is retrieved from disk and returned to the client.
   - **Blacklist Check**: If the URL is blacklisted, the proxy returns a custom error page.
   - **Forwarding Request**: If the page is not cached and not blacklisted, the proxy forwards the request to the web server, retrieves the response, caches it, and sends it to the client.
3. **Error Handling**: If the web server responds with a "404 Not Found" or another error, the proxy displays a custom error page.

## Configuration
### Blacklist URL Filter
- You can block specific URLs by adding them to the `URL_BLOCKED.txt` file. Each URL should be listed on a new line.

### Browser Configuration
- To configure the proxy settings in your browser:
  - **Chrome/Firefox**: Go to `Settings` > `Network` > `Proxy` and enter the proxy IP and port (e.g., `localhost:8888`).

