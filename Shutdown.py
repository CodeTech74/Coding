import os
import platform
import subprocess

def shutdown(delay=0):
    """
    Initiates a system shutdown.

    Args:
        delay: The delay in seconds before shutdown (default is 0).
    """
    os_name = platform.system()

    if os_name == "Windows":
        try:
            subprocess.run(["shutdown", "/s", "/t", str(delay)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during shutdown: {e}")
        except FileNotFoundError:
            print("Shutdown command not found (Windows).")

    elif os_name == "Linux" or os_name == "Darwin":  # Darwin is macOS
        try:
            subprocess.run(["shutdown", "-h", f"+{delay // 60}"], check=True) #shutdown -h +minutes
        except subprocess.CalledProcessError as e:
            print(f"Error during shutdown: {e}")
        except FileNotFoundError:
            print("Shutdown command not found (Linux/macOS).")

    else:
        print("Shutdown not supported on this operating system.")

# Example usage:
# Shutdown immediately:
# shutdown()

# Shutdown after 60 seconds:
# shutdown(60)

# Shutdown after 5 minutes
# shutdown(300)

def abort_shutdown():
    """
    Aborts a scheduled system shutdown.
    """
    os_name = platform.system()

    if os_name == "Windows":
        try:
            subprocess.run(["shutdown", "/a"], check=True)
            print("Shutdown aborted.")
        except subprocess.CalledProcessError as e:
            print(f"Error aborting shutdown: {e}")
        except FileNotFoundError:
            print("Shutdown command not found (Windows).")

    elif os_name == "Linux" or os_name == "Darwin":
        try:
            subprocess.run(["shutdown", "-c"], check=True)
            print("Shutdown aborted.")
        except subprocess.CalledProcessError as e:
            print(f"Error aborting shutdown: {e}")
        except FileNotFoundError:
            print("Shutdown command not found (Linux/macOS).")

    else:
        print("Shutdown abort not supported on this operating system.")

# Example usage to abort a shutdown:
# abort_shutdown()