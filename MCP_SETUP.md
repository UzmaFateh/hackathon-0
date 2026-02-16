# MCP Server Configuration Guide

## Overview

Model Context Protocol (MCP) servers extend Claude Code's capabilities by providing access to external tools, APIs, and services.

## Configuration File Location

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Linux:** `~/.config/Claude/claude_desktop_config.json`

## Basic Configuration Structure

```json
{
  "mcpServers": {
    "server-name": {
      "command": "command-to-run",
      "args": ["arg1", "arg2"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

## Recommended MCP Servers for AI Employee

### 1. File System Server

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:\\Users\\uzmaf\\OneDrive\\Documents\\AI_Employee_Vault"]
    }
  }
}
```

**Capabilities:**
- Read/write files
- List directories
- Search files
- Monitor changes

### 2. GitHub Server

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

**Capabilities:**
- Create/update issues
- Manage pull requests
- Search repositories
- Access GitHub API

### 3. Google Drive Server

```json
{
  "mcpServers": {
    "gdrive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gdrive"],
      "env": {
        "GOOGLE_CLIENT_ID": "your-client-id",
        "GOOGLE_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

**Capabilities:**
- Access Google Drive files
- Upload/download documents
- Share files
- Manage folders

### 4. Slack Server

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-token",
        "SLACK_TEAM_ID": "T1234567890"
      }
    }
  }
}
```

**Capabilities:**
- Send messages
- Read channels
- Manage threads
- Upload files

### 5. PostgreSQL/Database Server

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:password@localhost:5432/dbname"
      }
    }
  }
}
```

**Capabilities:**
- Execute queries
- Manage tables
- Run migrations
- Export data

### 6. Calendar Server (Google Calendar)

```json
{
  "mcpServers": {
    "calendar": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-calendar"],
      "env": {
        "GOOGLE_CLIENT_ID": "your-client-id",
        "GOOGLE_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

**Capabilities:**
- Create events
- Check availability
- Send invites
- Manage reminders

### 7. Email Server (Gmail)

```json
{
  "mcpServers": {
    "gmail": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gmail"],
      "env": {
        "GOOGLE_CLIENT_ID": "your-client-id",
        "GOOGLE_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

**Capabilities:**
- Send emails
- Read inbox
- Search messages
- Manage labels

### 8. Web Search Server

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-api-key"
      }
    }
  }
}
```

**Capabilities:**
- Web search
- News search
- Image search
- Real-time information

## Complete Example Configuration

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:\\Users\\uzmaf\\OneDrive\\Documents\\AI_Employee_Vault"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Custom MCP Server

Create your own MCP server for specialized needs:

```python
# custom_mcp_server.py
from mcp.server import Server
from mcp.types import Tool, TextContent

server = Server("custom-ai-employee")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="process_invoice",
            description="Process and categorize invoices",
            inputSchema={
                "type": "object",
                "properties": {
                    "invoice_path": {"type": "string"},
                    "amount": {"type": "number"}
                }
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "process_invoice":
        # Your custom logic here
        return [TextContent(type="text", text="Invoice processed")]

if __name__ == "__main__":
    server.run()
```

Add to config:
```json
{
  "mcpServers": {
    "custom-ai-employee": {
      "command": "python",
      "args": ["C:\\path\\to\\custom_mcp_server.py"]
    }
  }
}
```

## Security Best Practices

1. **Environment Variables**
   - Never commit API keys to version control
   - Use environment variables for sensitive data
   - Rotate keys regularly

2. **Permissions**
   - Grant minimum necessary permissions
   - Use read-only tokens when possible
   - Audit access regularly

3. **Validation**
   - Validate all inputs
   - Sanitize file paths
   - Check rate limits

## Troubleshooting

**Server not starting:**
```bash
# Check if npx is installed
npx --version

# Test server manually
npx -y @modelcontextprotocol/server-filesystem /path/to/vault
```

**Connection issues:**
- Verify API keys are correct
- Check network connectivity
- Review server logs

**Permission errors:**
- Ensure file paths are accessible
- Check environment variable syntax
- Verify token scopes

## Testing MCP Servers

```bash
# Test filesystem server
npx -y @modelcontextprotocol/server-filesystem C:\\Users\\uzmaf\\OneDrive\\Documents\\AI_Employee_Vault

# Test with Claude Code
claude code --test-mcp filesystem
```

## Useful MCP Resources

- Official MCP Documentation: https://modelcontextprotocol.io
- MCP Server Registry: https://github.com/modelcontextprotocol/servers
- Community Servers: https://github.com/topics/mcp-server

## Integration with AI Employee Workflow

### Inbox Processing
Use filesystem MCP to monitor and process inbox items automatically.

### External Communication
Use Slack/Email MCP to send notifications and updates.

### Data Access
Use database MCP to query and update business data.

### Research
Use web search MCP to gather current information.

### Calendar Management
Use calendar MCP to schedule tasks and meetings.

## Next Steps

1. Install Node.js (required for npx)
2. Choose relevant MCP servers for your workflow
3. Obtain necessary API keys
4. Update configuration file
5. Restart Claude Code
6. Test each server
7. Update agent skills to use MCP capabilities
