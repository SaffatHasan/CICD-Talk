---
theme: default
marp: true
footer: Intro to CICD
---

# Intro to CICD

![bg left](https://source.unsplash.com/Tjbk79TARiE)

---

# Contents

- What is CICD?
- How is it Useful?
- Demo
- Pros & Cons

![bg right](https://source.unsplash.com/huT1A8nW_Ho)

---

# What is CICD?

- Continuous Integration
- Continuous Deployment
- Developer + Operations (DevOps)

![bg left fit](https://software.af.mil/wp-content/uploads/2019/08/devops-loop.svg)

---

# How is it Useful?

- Slowing down is boring
- Focus on the important stuff
- Let the robots handle the rest

![bg right](https://source.unsplash.com/WR-ifjFy4CI)

---

# How is it Useful?

- Check style and unit testing
- Automate deployments
- Automate rollbacks
- Don't call me at 4am

![bg left](https://source.unsplash.com/HBGYvOKXu8A)

---

# Demo

- Build resume using LaTeX
- Build slides using Marp

![bg right](https://source.unsplash.com/lB9ylP8e9Sg)

---

# Demo

- PyLint checks style
- Python builds resume.tex
- Latex builds resume.pdf
- Marp builds slides.html
- Github Actions deploys them to gh-pages

![bg right](https://source.unsplash.com/lB9ylP8e9Sg)

---

# Demo

Can you make it better?

- Multiple templates?
- Deploy to a real static page?
- Deploy to s3?

![bg left](https://source.unsplash.com/RNoiGmxhf7Y)

---

# Pros

- 0 effort deployments
- Pretty green buttons

![bg right](https://source.unsplash.com/p-I9wV811qk)

---

# Cons
<style scoped>
    pre {
        font-size: 2rem;
    }
</style>

```bash
alias fuck='git add .; git commit --amend --no-edit; git push -f'
```
- Hard to unify enterprise
- Build it twice
- YAML
- Who tests the tests?
- Many, many tools
    - Github Actions
    - Gitlab CI
    - Bitbucket Pipelines
    - etc.

![bg left](https://source.unsplash.com/bmJAXAz6ads)

---

# Links

- [saffathasan.github.io/CICD-Talk](https://saffathasan.github.io/CICD-Talk)
- [saffathasan.github.io/CICD-Talk/resume.pdf](https://saffathasan.github.io/CICD-Talk/resume.pdf)
- [Github Actions](https://github.com/features/actions)
- [Marp](https://marp.app)
- [Resume How-To](https://www.freecodecamp.org/news/writing-a-killer-software-engineering-resume-b11c91ef699d/)
