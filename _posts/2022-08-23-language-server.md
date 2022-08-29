--- 
layout: page
title: Language servers
category: notes
tags: [programming,productivity]
excerpt: Language servers provide IDE-like capabilities to editors like Vim.
---

**I'll update this when I do a fresh install of Fedora and set things up. This is for a rather old version of Ubuntu (18.04.6).**

You might want to use a language server if you want IDE-like capabilities built into vim. 
Here's how I set up my language servers for C++ and Python.

# Prerequisites: Neovim (not required!) and language server packages.

You don't need Neovim (`nvim`) to use a language server, but I used Neovim, so that's what's here. 
[Here's how I set up Neovim]({% post_url 2022-08-13-neovim.md %}).

## C++ language servers.

You'll also want `llvm` and `clangd-10`. 
`llvm` was already set up on Ubuntu-18.04.6. 
I'll update this once I do a fresh install with Fedora, but I was able to install this using `apt-get`. 
```
sudo apt-get install clangd-10
```
Not the most recent version of `clangd`, but it'll have to do.

This is the language server for C++.

## Python language servers.

For python, Niels uses `python-lsp-server` and `pyright-langserver`. 
I couldn't get this working on my setup, because everything was too old. 
I'll update this when I upgrade my Linux distro. 

## Plug for Neovim.

[Plug](https://github.com/junegunn/vim-plug) is a super simple package manager for VIM and Neovim. 
The instruction from their README that I used is 
```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```
This should download a file in `${HOME}/.local/share/nvim/site/autoload/plug.vim`.

# Adding language server functionality to Neovim.

Now that plug is installed, you should issue the command in `nvim`:
```
:PlugInstall nvim-lspconfig
```
and then put:
```
call plug#begin()
Plug 'neovim/nvim-lspconfig'
call plug#end()
```
in your `.vimrc`. 

The language server settings are found in the `init.vim` of [my dotfiles](https://github.com/bbusemeyer/dotfiles), which are pretty much a copy-paste of the same file from [Niels' dotfiles](https://github.com/Wentzell/dotfiles). 

I'll annotate that at some point!

# Giving the language server what it wants: C++. 

You need to make a special file, `compile_commands.json`, which is just a record of the commands used to compile your C++ library.

One way to do this uses CMake. 
When you do your normal `cmake` command, use the following flag:
```
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```
Then, `compile_commands.json` will appear in your build directory. 
Unfortunately, this will not contain what is needed to hop to a header file. 
For that, you need to append the header information to it. 
A script is available for that:
```
pip install --user compdb
```
Then, 
```
compdb -p build/ list > compile_commands.json
```
where `build/` is supposed to be the path to your CMake build directory, will append the header information and make a new `compile_commands.json` with that in it. 

Now issue a command like:
```
nvim **/*.cpp **/*.cu **/*.hpp **/*.hxx **/*.h
```
to open all the files in your project. 
You can use `:b <file>` to jump around to different files that way. 
Try using `ctrl-[` on a function or object, even ones defined in the standard lib. 
You'll see that you've jumped to it's definition!

I'll add more tricks with it as I use it (and finish annotating the `init.vim` file for Neovim!).

# Giving the language server what it wants: Python.

**Will update when Python language servers are working on my setup!**
*I think??* you just open the Python files that are involved in your project, and it should allow you to follow references just like that! 
Python is magical like that.
