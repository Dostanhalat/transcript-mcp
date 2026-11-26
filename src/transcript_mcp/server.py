"""MCP server entry point. Speaks MCP over stdio, so nothing here may print to stdout."""

from mcp.server import MCPServer

mcp = MCPServer("transcript-mcp")


@mcp.tool()
def list_transcripts() -> list[str]:
    """List the transcripts in the index. Always empty until indexing exists."""
    return []


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
