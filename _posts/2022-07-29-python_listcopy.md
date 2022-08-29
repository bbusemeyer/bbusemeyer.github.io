---
layout: page
title: Copying a list vs. editing.
category: notes
tags: [programming,Python]
excerpt: A peculiarity of Python that I found interesting or useful. 
---

Sometimes you want to replace a list's contents without reassigning the pointer of the variable. 
For example, you are creating an [unpure function](https://en.wikipedia.org/wiki/Pure_function).

I was looking over [this post](https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk). 

It suggested the following code for modifying a list, in place
```
exclude = set(['New folder', 'Windows', 'Desktop'])
for root, dirs, files in os.walk(top, topdown=True):
    dirs[:] = [d for d in dirs if d not in exclude]
```
Here, the `dirs[:]` syntax ensures that the reference to `dirs` in `os.walk` is modified, rather than having the name reassigned. 
If you simply assigned, `dirs = ...`, then `dirs` would point to a new address and `os.walk` would continue using the list at the old address, effectively ignoring the change. 
Using the slice operator ensures the pointer stays the same and the contents are modified in-place. 
