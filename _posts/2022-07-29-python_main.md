--- 
layout: page
title: Using a `main` function in Python.
category: notes
tags: [programming,Python]
excerpt: Peculiarities of Python that I found interesting or useful. 
---

# `if __main__` and keeping the global namespace clean. 

In a lot of examples of python code I've seen, people often do something like:
```
def foo(testval):
  if testval=='foo':
    return 'bar'
  else:
    return 'no'

if __name__ == '__main__':
  testval = 'foo'
  foo(testval)
```
`testval` is now defined in both global and local scope, which is fine, because the local scope will override the global one. 
But say you accidentally made a typo:
```
def foo(testval):
  if test=='foo': # oops
    return 'bar'
  else:
    return 'no'

if __name__ == '__main__':
  test = 'foo'
  print("I will not test", test)
  foo('bar')
```
Then the code will silently run and use the global variable `test` and ignore the input variable `testvar`. 

To avoid this, I avoid defining anything in the global scope.
```
def main():
  test = 'foo'
  print("I will not test", test)
  foo('bar')

def foo(testval):
  if test=='foo': # oops
    return 'bar'
  else:
    return 'no'

if __name__ == '__main__':
  main()
```
Now, the code will error on this typo because `test` is not defined anywhere. There's an added bonus that the first lines of code that are executed are at the top of the file, which makes more sense to me than the bottom. 
