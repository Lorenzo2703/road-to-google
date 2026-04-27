import json
import os

def create_notebook(path, title, day, topic, theory_md, problems, is_coding=True):
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# Day {day:02d}: {title}\n",
                "\n",
                f"**{topic}**\n",
                "\n",
                "---\n",
                "\n",
                "## 📚 Theory: Deep Dive\n",
                "\n"
            ] + [line + "\n" for line in theory_md.split("\n")]
        }
    ]
    
    if is_coding and problems:
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 🔨 Hands-on Labs\n"]
        })
        for i, prob in enumerate(problems, 1):
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"### Lab {i}: {prob['name']}\n", "\n"] + [line + "\n" for line in prob.get('desc', '').split('\n')]
            })
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + "\n" for line in prob.get('code', 'def solve():\n    pass').split('\n')]
            })

    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"## 📝 Day {day} Mastery Checklist\n",
            "\n",
            "- [ ] Explain the difference between `fork()` and `vfork()`.\n",
            "- [ ] Identify a process in `D` state (uninterruptible sleep) and explain why it can't be killed.\n",
            "- [ ] Use `strace` to identify a missing shared library.\n",
            "- [ ] Calculate the impact of context switching on a high-throughput service.\n"
        ]
    })

    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

# --- Day 29 CONTENT ---
DAY_29_THEORY = """
### 1. The Process Lifecycle
Every process in Linux is created by another process (except `init`/`systemd`).
- **fork()**: Creates a child process by duplicating the calling process. The child gets a new PID.
- **exec()**: Replaces the current process image with a new one (e.g., running `ls`).
- **wait()**: Parent waits for child to finish to collect its exit status.
- **Zombie Processes**: A child that has finished but its parent hasn't called `wait()` yet.

### 2. System Calls (The Interface)
Syscalls are the only way to transition from User Space to Kernel Space.
- **File I/O**: `open`, `read`, `write`, `close`, `lseek`.
- **Process Mgmt**: `fork`, `execve`, `exit`, `getpid`.
- **Memory**: `mmap`, `brk`, `munmap`.
- **Networking**: `socket`, `bind`, `connect`, `send`, `recv`.

### 3. File Descriptors & Standard Streams
- `0`: stdin
- `1`: stdout
- `2`: stderr
- Everything is a file: Pipes, Sockets, and Hardware devices are all accessed via FDs.

### 4. Signals: Kernel-to-Process Communication
- `SIGINT` (2): Interrupt from keyboard (Ctrl+C).
- `SIGTERM` (15): Graceful termination request (Default for `kill`).
- `SIGKILL` (9): Immediate termination (Cannot be caught or ignored).
- `SIGCHLD`: Sent to parent when child dies.
"""

DAY_29_PROBLEMS = [
    {
        "name": "The Zombie Hunter",
        "desc": "Write a Python script that spawns a child process, lets it finish, but the parent sleeps for 10 seconds without calling wait. Observe the zombie state in `ps aux`.",
        "code": """import os
import time

pid = os.fork()
if pid > 0:
    print(f'Parent {os.getpid()} sleeping... Check "ps aux | grep {pid}" for Z state')
    time.sleep(10)
    os.wait() # Clean up zombie
    print('Parent cleaned up child.')
else:
    print(f'Child {os.getpid()} exiting immediately.')
    os._exit(0)"""
    },
    {
        "name": "Tracing a Mystery Failure",
        "desc": "Explain how you would use `strace -e open python script.py` to find exactly which file a Python script is failing to find, even if the error message is vague.",
        "code": "# Discussion: strace catches the 'ENOENT (No such file or directory)' error from the open() syscall."
    }
]

if __name__ == '__main__':
    create_notebook(
        path='week-05-cloud-sre/day-29-linux-internals.ipynb',
        title="Linux Internals: Processes & Syscalls",
        day=29,
        topic="Week 5 — Cloud SRE",
        theory_md=DAY_29_THEORY,
        problems=DAY_29_PROBLEMS
    )
    print("Regenerated Day 29 with extreme detail.")
