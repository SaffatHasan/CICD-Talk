# Introduction to CICD

![bg left](https://source.unsplash.com/Tjbk79TARiE)

---

# Table of Contents

- What is CICD?
- How is it useful?
- Demo
- Pros
- Cons
- Links

![bg right](https://source.unsplash.com/huT1A8nW_Ho)

---

# What is CICD?

- Continuous Integration
- Continuous Deployment
- Developer + Operations (DevOps)

![bg left fit](https://software.af.mil/wp-content/uploads/2019/08/devops-loop.svg)

---

# How is it useful?

- Slowing down is boring
- Focus on the important stuff
- Let the robots handle the rest

![bg right](https://source.unsplash.com/WR-ifjFy4CI)

---

# How is it useful?

- Check style and unit testing
- Automate deployments
- Automate rollbacks
- Don't call me at 4am

![bg left](https://source.unsplash.com/HBGYvOKXu8A)

---

# Demo

- Building a resume locally
- Build it using Github Actions

---

# Demo

- Can you make it better?
- Support multiple templates?
- Deploy to a real static page?
- Autogenerate S3 bucket (terraform) and have a DNS record point to it?

![bg left](https://source.unsplash.com/RNoiGmxhf7Y)

---

# Pros

- Never have to copy/paste your PDF
- Pretty green button lets you know nothing is broken

![bg right](https://source.unsplash.com/p-I9wV811qk)

---

# Cons
<style scoped>
    pre {
        font-size: 2rem;
    }
</style>

- Can be hard to setup
```bash
alias fuck='git add .; git commit --amend --no-edit; git push -f'
```

- Hard to scale across the enterprise
- Setup varies
    - Github Actions
    - Gitlab CI
    - Bitbucket Pipelines
    - etc.

![bg left](https://source.unsplash.com/bmJAXAz6ads)

---

# Links