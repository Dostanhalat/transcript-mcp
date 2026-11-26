import sys

import pytest
from mcp import Client, StdioServerParameters

pytestmark = pytest.mark.anyio


async def test_exposes_expected_tools(client):
    result = await client.list_tools()
    assert [t.name for t in result.tools] == ["list_transcripts"]


async def test_list_transcripts_starts_empty(client):
    result = await client.call_tool("list_transcripts", {})
    assert not result.is_error
    assert result.structured_content == {"result": []}


async def test_real_stdio_process_starts():
    # Launches the server as a subprocess, the same way Claude Desktop does.
    params = StdioServerParameters(command=sys.executable, args=["-m", "transcript_mcp.server"])
    async with Client(params) as c:
        result = await c.list_tools()
    assert [t.name for t in result.tools] == ["list_transcripts"]
