name: Generate contribution snake

on:
schedule:
# 每天 UTC 00:15 自动更新
- cron: "15 0 * * *"

# 允许在 Actions 页面手动运行

workflow_dispatch:

# 修改主分支后也运行一次

push:
branches:
- main

permissions:
contents: write

jobs:
generate:
runs-on: ubuntu-latest
timeout-minutes: 5

```
steps:
  - name: Generate contribution snake
    uses: Platane/snk/svg-only@v3
    with:
      github_user_name: ${{ github.repository_owner }}

      outputs: |
        dist/github-contribution-grid-snake.svg?palette=github-light&color_snake=%2357606a
        dist/github-contribution-grid-snake-dark.svg?palette=github-dark&color_snake=%238b949e

  - name: Publish SVG files to output branch
    uses: crazy-max/ghaction-github-pages@v5
    with:
      target_branch: output
      build_dir: dist
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
