--- 
layout: page
title: Git submodules
category: notes
tags: [programming,productivity,practices]
excerpt: Git submodules let you have a repo in a repo.
---

Submodules in git are used for including a repo inside another repo.
The intended use case is when you want to maintain a specialized branch of another repo within a repo.
That way, you can keep the commits separate between the projects, but still push joint commits between the projects.

A nice use case other than this is the following. 
Let's say you want to make cloning and using repo _A_ super easy. 
_A_ depends on repo _B_, but no other code is expected to. 
For example, you want to have [`vim-plug`](https://github.com/junegunn/vim-plug) included in [your configuration repo](https://github.com/bbusemeyer/dotfiles).
You know `vim-plug` will not need to be shared with any other project, so why not keep it in `dotfiles`?
Including it as a submodule allows you to clone _A_ (`dotfiles`) and _B_ (`vim-plug`) at the same time, and even specify a commit of _B_ for posterity. 

# Basics on getting started

Cloning the repo as a submodule:
```
git submodule add <remote>
```
Now you can navigate to that repo and treat it as a separate repo from the containing one. 

[A good reference for more details in using submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

