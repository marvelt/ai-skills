from mcp.server.fastmcp import FastMCP
import subprocess

mcp = FastMCP("vps-security")


@mcp.tool()
def get_system_info() -> str:
    """Return basic read-only information about the VPS."""
    commands = {
        "os": ["cat", "/etc/os-release"],
        "kernel": ["uname", "-r"],
        "cpu": ["lscpu"],
        "memory": ["free", "-h"],
    }

    result = []

    for name, command in commands.items():
        try:
            output = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=10,
                check=False,
            )
            result.append(f"=== {name} ===\n{output.stdout}")
        except Exception as e:
            result.append(f"=== {name} ===\nERROR: {e}")

    return "\n".join(result)


@mcp.tool()
def get_docker_containers() -> str:
    """Return currently running Docker containers, read-only."""
    command = [
        "docker",
        "ps",
        "--format",
        "{{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Status}}",
    ]

    try:
        output = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )

        if output.returncode != 0:
            return f"ERROR: {output.stderr.strip()}"

        return output.stdout or "No running containers."

    except Exception as e:
        return f"ERROR: {e}"


@mcp.tool()
def get_listening_ports() -> str:
    """Return locally listening TCP/UDP sockets, read-only."""
    command = ["ss", "-tulpen"]

    try:
        output = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )

        if output.returncode != 0:
            return f"ERROR: {output.stderr.strip()}"

        return output.stdout

    except Exception as e:
        return f"ERROR: {e}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
