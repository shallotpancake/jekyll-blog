# Personal Jekyll Blog

A fully-featured Jekyll blog with easy management tools, customization options, and deployment instructions.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Managing Posts](#managing-posts)
  - [Blog Management Script](#blog-management-script)
- [Customization](#customization)
- [Deployment](#deployment)
- [Directory Structure](#directory-structure)
- [Advanced Configuration](#advanced-configuration)

## Features

- 🚀 Fast and lightweight static site
- 📱 Responsive design using Minima theme
- 🔍 SEO optimized with jekyll-seo-tag
- 📑 Pagination support
- 🏷️ Categories and tags with archives
- 📰 RSS feed
- 🎨 Syntax highlighting for code blocks
- 📝 Easy post management with Python script
- 🔄 Live reload during development

## Prerequisites

Before you begin, ensure you have the following installed:
- Ruby (version 2.5.0 or higher)
- RubyGems
- GCC and Make
- Python 3.x (for the management script)

### Installing Prerequisites

#### On Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install ruby-full build-essential zlib1g-dev python3
```

#### On macOS:
```bash
# Using Homebrew
brew install ruby python3
```

#### On Windows:
1. Install Ruby using [RubyInstaller](https://rubyinstaller.org/)
2. Install Python from [python.org](https://www.python.org/)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd my_blog
```

2. Install Jekyll and dependencies:
```bash
gem install bundler
bundle install
```

3. Make the management script executable:
```bash
chmod +x manage_blog.py
```

## Usage

### Managing Posts

The blog comes with a Python management script that makes it easy to create and manage posts.

```bash
# Start the blog server
./manage_blog.py start

# Create a new post
./manage_blog.py new "Your Post Title"

# List all posts
./manage_blog.py list

# Stop the blog server
./manage_blog.py stop
```

### Writing Posts

Posts are written in Markdown and stored in the `_posts` directory. Each post should have front matter at the top:

```markdown
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD
categories: [category1, category2]
tags: [tag1, tag2]
---

Your post content here...

<!--more-->

Rest of your post...
```

The `<!--more-->` tag determines what shows up as the excerpt on the main page.

## Customization

### Site Configuration

Edit `_config.yml` to customize your blog's settings:

```yaml
# Basic Settings
title: "Your Blog Title"
description: "Your blog description"
author: "Your Name"

# Social Links
github_username: your-username
twitter_username: your-username

# Build Settings
show_excerpts: true
paginate: 5
```

### Theme Customization

This blog uses the Minima theme. To customize it:

1. Create a `_sass` directory if it doesn't exist
2. Create your custom CSS in `_sass/custom.scss`
3. Import it in `assets/main.scss`:

```scss
---
---

@import "minima";
@import "custom";
```

## Deployment

### GitHub Pages

1. Create a repository on GitHub
2. Update the `_config.yml`:
```yaml
baseurl: "/repository-name"
url: "https://username.github.io"
```

3. Push to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/repository-name.git
git push -u origin main
```

### Custom Server

1. Build the site:
```bash
JEKYLL_ENV=production bundle exec jekyll build
```

2. The static site will be in the `_site` directory

3. Deploy using nginx:
```bash
# Install nginx
sudo apt-get install nginx

# Create nginx configuration
sudo nano /etc/nginx/sites-available/blog
```

Add this configuration:
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    root /path/to/your/blog/_site;
    
    location / {
        try_files $uri $uri/ =404;
    }
}
```

4. Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Automatic Deployment with GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy Blog

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Ruby
      uses: ruby/setup-ruby@v1
      with:
        ruby-version: 3.0
        
    - name: Install dependencies
      run: |
        gem install bundler
        bundle install
        
    - name: Build site
      run: JEKYLL_ENV=production bundle exec jekyll build
        
    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./_site
```

## Directory Structure

```
my_blog/
├── _posts/          # Blog posts
├── _layouts/        # Layout templates
├── _includes/       # Reusable components
├── _sass/          # Custom CSS
├── assets/         # Static files
├── _site/         # Generated site
├── _config.yml    # Site configuration
├── Gemfile        # Ruby dependencies
├── manage_blog.py # Management script
└── README.md      # This file
```

## Advanced Configuration

### Adding Comments

To add Disqus comments:

1. Sign up for Disqus
2. Add to `_config.yml`:
```yaml
disqus:
  shortname: your-disqus-shortname
```

### Adding Analytics

To add Google Analytics:

1. Get your tracking ID
2. Add to `_config.yml`:
```yaml
google_analytics: UA-XXXXXXXX-X
```

### Custom Domain

1. Create a `CNAME` file in the root directory:
```
yourdomain.com
```

2. Update DNS settings with your provider:
```
A record: @ -> GitHub Pages IP
CNAME: www -> username.github.io
```

## Troubleshooting

### Common Issues

1. **Jekyll build errors**
   - Check Ruby version: `ruby -v`
   - Update dependencies: `bundle update`

2. **Management script issues**
   - Ensure Python 3 is installed: `python3 --version`
   - Check file permissions: `chmod +x manage_blog.py`

3. **Live reload not working**
   - Check port 4000 is not in use
   - Restart the server: `./manage_blog.py stop && ./manage_blog.py start`

For more help, check the [Jekyll documentation](https://jekyllrb.com/docs/) or create an issue in the repository.