<div align="center">

  # Hi 👋, I'm Vinícius José
> *"I am not in competition with anyone but myself. My goal is to improve myself continuously."*  
  > **— Bill Gates**

  <p align="center">
    <b>Software Engineering Student | Focus on DevOps & Cloud</b>
  </p>

  [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=18&pause=1000&color=BD93F9&center=true&vcenter=true&width=500&lines=Building+software+solutions...;Learning+and+improving+everyday...;Continuous+Improvement+%7C+Bill+Gates)](https://git.io/typing-svg)

  <br />

  <!-- Social Badges Minimalistas no Tema Dracula -->

  <a href="https://www.linkedin.com/in/viniciussj77" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-282A36?style=for-the-badge&logo=linkedin&logoColor=BD93F9" alt="LinkedIn" />
  </a>

  <a href="https://instagram.com/viniciussj77" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-282A36?style=for-the-badge&logo=instagram&logoColor=FF79C6" alt="Instagram" />
  </a>

  <a href="https://mail.google.com/mail/?view=cm&fs=1&to=vjbezerra2007@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-282A36?style=for-the-badge&logo=gmail&logoColor=8BE9FD" alt="Gmail" />
  </a>

</div>

<br />

---
<div align="center">
  <a href="https://github.com/Viniciussj77">
  <img height="160em" src="https://github-readme-stats.vercel.app/api?username=Viniciussj77&show_icons=true&theme=dracula&include_all_commits=true&count_private=true"/>
  <img height="140em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Viniciussj77&layout=compact&langs_count=7&theme=dracula"/>
</div>

<div>
  name: Generate Datas

on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch:

jobs:
  build:
    name: Jobs to update datas
    runs-on: ubuntu-latest

  steps:
      # Snake Animation
      - uses: Platane/snk@master
        id: snake-gif
        with:
          github_user_name: Viniciussj77
          svg_out_path: dist/github-contribution-grid-snake.svg

   - uses: crazy-max/ghaction-github-pages@v2.1.3
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
</div>

### 🚀 About Me

<br>

<div align="center">
  <img alt="JavaScript" height="40" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-plain.svg">
  <img alt="HTML5" height="40" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg">
  <img alt="CSS3" height="40" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg">
  <img alt="Python" height="40" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img alt="Docker" height="40" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg">
  <img alt="Linux" height="40" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg">
</div>
