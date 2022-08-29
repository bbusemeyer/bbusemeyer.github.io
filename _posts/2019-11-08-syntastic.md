--- 
layout: page
title: Installing and using syntastic.
category: notes
tags: [vim,productivity]
excerpt: Syntastic will alert you to syntax errors before compilation or running the code, saving you time.
---
Syntastic will alert you to syntax errors before compilation or running the code, saving you time.
No, you don't need to use an IDE for syntax correction!

I used [vundle]({% post_url 2019-11-08-vundle %}) to install it in one command.
Then edit your `vimrc` according to [their instructions](https://github.com/vim-syntastic/syntastic#settings), so that it has newbie setup (which worked for me):
```
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
```

After that, things worked perfectly.

This will also enable it to use it's built-in syntax checkers.
There's information on its page about how to add additional checkers.

# Later troubleshooting

## Missing C++ headers. 

I encountered an issue with syntastic flagging missing C++ headers that were actually in another directory. 
This turned out to be fixable with adding 
```
let g:syntastic_c_include_dirs = [ '../include', 'include' ]
```
to my `.vimrc`, which tells Vundle to look there for headers. 

This only works if you are willing to list out all the header locations, which I quickly found to be annoying as hell.
When you get to that point,
```
let g:syntastic_c_remove_include_errors=1
```

## Python version control.

Another fixable issue was updating the python syntax to python3. 
I had to to a `pip3 install --user pyflakes` and then set

```
let g:syntastic_python_checkers = ['pyflakes']
```

It's also possible to define functions to switch this as needed.
