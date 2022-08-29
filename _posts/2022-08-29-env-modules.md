--- 
layout: page
title: Environment modules
category: notes
tags: [programming,productivity]
excerpt: Environment modules to easily modify and maintain your shell environment
---

[Environment modules](http://modules.sourceforge.net/) is a tool that allows you to modify and reverse modifications to important enviroment variables like `PATH` and `PYTHONPATH`.
You'd want to keep track of this if you swap between different libraries when compiling or running code (i.e. between GNU and Intel compilers) or if you want to avoid namespace clashes between different libraries or libraries of different versions.

# Simple examples.

Let's say you want to build your C++ code with GNU and Intel and check which one is faster and by how much.
You'd have [set up a modulefile](#Making a modulefile) for GNU and one for Intel, then you can do the following:
```
mkdir build-intel
cd build-intel
module load intel/3.0.1
cmake .. && make # e.g. build your library
cd ..
mkdir build-gnu
cd build-gnu
module unload intel
module load gnu/4.2.1
cmake .. && make # e.g. build your library
```
Now, whenever you want one version or the other, simply load the correct module and run the executible.

# Setup on Manjaro Linux

The install process involves:
 * Installing with a package manager or compiling the source.
 * Sourcing the relevant script for setting things up (no `module` command will be available until you do).
 * (Probably) adding that script to your basic initialization for the shell.

On Manjaro (or any Arch), I started with 
```
pamac build env-modules
```
Different package managers may have different commands or names, but most of them have Environment Modules somewhere, you just have to look around.

The `module` command won't work until you've sourced the initialization script. 
Where that script is depends on how you installed it, or how your package manager installed it. 

I found where by issuing
```
pamac list -f env-modules
```
which listed all the files associated with `env-modules`.
In that list, I found `/etc/modules/init/zsh`. 

```
source /etc/modules/init/zsh
module --version
module avail
```
And I saw things were working. 
I then added 
```
source /etc/modules/init/zsh
```
to [my `.zshrc`](https://github.com/bbusemeyer/dotfiles/blob/manjaro/config/zshrc).
From now on, `modules` command will be ready to go at shell start up.

# Making a modulefile

I use the following organization for module files:
```
#%Module
set     pkg         gem
set     version     3.0.0
set     root        /home/brian/.local/share/gem/ruby/${version}/bin

module-whatis   "Sets the environment for $pkg-$version"
proc ModulesHelp { } {
    puts stderr "Sets the environment for $pkg-$version"
}

prepend-path  PATH $root
```
You would replace `gem` with your module's name, and `3.0.0` with whatever version you'd like to name it.
`root` is an optional variable, which just cleans up the commands at the bottom. Obviously, you'd want to change that path to wherever you want to append to the `PATH`.
This sets up a module `gem` and when I `module load gem`, then it will prepend the `PATH` with the gem executible locations. 
[Other types of environment modifications are possible.](https://modules.readthedocs.io/en/latest/cookbook.html), including enforcing conflicts and so on. 
You can also issue module load commands here to create module dependencies. 

Place the file like that in your software folder, which I call `~/soft`, following [Paul Yang's](paul-st-young.github.io/) convention.
So, it will be placed in `~/soft/modulefiles/gem/3.0.0`. 
You need to tell `module` where to look for it.
Do that by appending the `MODULEPATH` (probably in your `.rc` file, like `.zshrc`) 
```
export MODULEPATH=${HOME}/soft/modulefiles:$MODULEPATH
```

Now, issue
```
module avail
```
You should see a new module is available for you to `load` and `unload`.
