#!/usr/bin/env python3
import os
import sys
import datetime
import subprocess
import signal
import time

def create_post(title):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f"{date}-{'-'.join(title.lower().split())}.md"
    filepath = os.path.join('_posts', filename)
    
    if os.path.exists(filepath):
        print(f"Error: Post '{filename}' already exists!")
        return
    
    with open(filepath, 'w') as f:
        f.write(f"""---
layout: post
title: "{title}"
date: {date}
categories: blog
---

Write your post content here...
""")
    print(f"Created new post: {filepath}")

def list_posts():
    if not os.path.exists('_posts'):
        print("No posts directory found!")
        return
    
    posts = os.listdir('_posts')
    if not posts:
        print("No posts found!")
        return
    
    print("\nExisting posts:")
    for post in sorted(posts):
        print(f"- {post}")

def start_server():
    print("Starting Jekyll server...")
    with open('server.log', 'w') as log:
        subprocess.Popen(['bundle', 'exec', 'jekyll', 'serve', '--livereload'],
                        stdout=log,
                        stderr=log)
    print("Server started! View your blog at http://localhost:4000")
    print("Server logs are being written to server.log")

def stop_server():
    try:
        output = subprocess.check_output(['pgrep', '-f', 'jekyll serve'])
        pid = int(output.decode().strip())
        os.kill(pid, signal.SIGTERM)
        print("Server stopped!")
    except:
        print("No server found running!")

def show_help():
    print("""
Blog Management Commands:
    start   - Start the Jekyll server
    stop    - Stop the Jekyll server
    new     - Create a new blog post (followed by post title)
    list    - List all existing posts
    help    - Show this help message
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)

    command = sys.argv[1].lower()
    
    if command == "start":
        start_server()
    elif command == "stop":
        stop_server()
    elif command == "new":
        if len(sys.argv) < 3:
            print("Error: Please provide a post title!")
            sys.exit(1)
        create_post(" ".join(sys.argv[2:]))
    elif command == "list":
        list_posts()
    elif command == "help":
        show_help()
    else:
        print(f"Unknown command: {command}")
        show_help()
        sys.exit(1)