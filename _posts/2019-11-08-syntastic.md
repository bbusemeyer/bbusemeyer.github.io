--- 
layout: single
title: Installing and using syntastic.
category: notes
tags: [vim,productivity]
excerpt: Syntastic will alert you to syntax errors before compilation or running the code, saving you time.
---

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
