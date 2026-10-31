import sys
import asyncio
print("Testing MCP connection...", flush=True)

from smolagents import MCPClient
print("MCPClient imported", flush=True)

try:
    print("Connecting to MCP server...", flush=True)
    client = MCPClient({"url": "http://127.0.0.1:7860/gradio_api/mcp/sse", "transport": "sse"})
    print("Connected!", flush=True)
    tools = client.get_tools()
    print(f"Tools found: {[t.name for t in tools]}", flush=True)
    client.disconnect()
    print("Disconnected successfully", flush=True)
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}", flush=True)
    sys.exit(1)
