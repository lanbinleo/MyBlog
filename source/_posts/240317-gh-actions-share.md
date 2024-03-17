---
title: Hexo Github 自动部署和一些踩坑经验
tags:
  - Blog
  - Hexo
  - Github
categories: 
  - Config
abbrlink: 97df2bec
date: 2024-03-17 10:39:55
---

## 前言

这两天在捣鼓Hexo博客。我就在想，如果每次写完博客，我该如何发布到网上去呢？我第一个想到的就是Github pages的静态文件托管，但是每次都要手动执行`hexo clean && hexo g && hexo d`，这样太麻烦了。于是我就想到了Github Actions。

## 配置分享

在经过了无数次的失败后，我终于成功了。我将我的配置分享出来，希望对你有所帮助。

```yaml
name: Deploy Hexo

on:
  push:
    branches:
      - main  # 或者你使用的是master分支，就改为master

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: Setup Node.js
      uses: actions/setup-node@v1
      with:
        node-version: '21' # 可以根据需要选择Node.js的版本

    - name: Cache dependencies
      uses: actions/cache@v2
      with:
        path: ~/.npm
        key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
        restore-keys: |
          ${{ runner.os }}-node-

    - name: Install Dependencies
      run: |
        npm install hexo -g
        npm install
        git clone https://github.com/saicaca/hexo-theme-vivia.git themes/vivia
        npm install colorjs.io stylus hexo-symbols-count-time

    - name: Generate static pages
      run: hexo generate

    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./public  # Hexo默认生成的目录
```

这个actions比较好看懂。

1. 首先是`on`，表示在什么时候执行这个actions。这里是在push到main分支的时候执行。
2. `jobs`就是你这个actions要执行的任务。这里只有一个任务，叫`deploy`。
3. `runs-on`表示这个任务要在什么环境下执行。这里是在ubuntu-latest下执行。
4. `steps`就是这个任务要执行的步骤。这里有6个步骤。
    - `actions/checkout@v2`是用来checkout代码的（其实我也不知道有啥用）。
    - `actions/setup-node@v1`是用来安装Node.js的，版本按照你的需求修改。
    - `actions/cache@v2`是用来缓存依赖的，如果你的主机上已经有了依赖，就不用再安装了。
    - `npm install`是用来安装依赖的，这个地方要根据不同的主题做定制化的修改，我这里是vivia。
    - `hexo generate`是用来生成博客静态文件的。
    - `peaceiris/actions-gh-pages@v3`是用来将你的静态文件发布到Github Pages上的。

## 踩坑！

有一些小的容易踩坑的点，比如如果发现每次部署之后自定义pages域名被刷掉了，可以在`source`文件夹中添加CNAME文件，这样就可以保证每次部署之后自定义pages域名不会被刷掉（hexo会复制这个文件到部署目录）。