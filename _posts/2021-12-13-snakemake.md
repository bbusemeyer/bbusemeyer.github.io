--- 
layout: page
title: My take on Snakemake 
category: notes
tags: [code,tools,productivity,workflow]
excerpt: My take on the Snakemake pythonic tool for workflows. 
---

# Basic concept. 

[Workflow](https://en.wikipedia.org/wiki/Workflow) scripts are for stitching together different programs or scripts that are interconnected in a directed graph by their inputs and outputs.  

A simple example might be a script that prepares a molecule for a calculation, a calculation that produces volumes of raw data, and a third script that analyses the raw data into a more interpretable result.  

If you have this basic pattern being run for a variety of parameters, and execution behaves like a tree (with one script's results being used for many different other runs), then some organized management is probably useful.

People often write their own custom scripts to manage workflows, either in Bash or Python, but there are some good reasons to use a package like Snakemake:
* Good habits are enforced by learning workflow design patterns. 
* Workflows automatically scale to multiple nodes and [even cloud computing](https://snakemake.readthedocs.io/en/stable/executing/cloud.html). 
* Documentation for your workflow script already exists because Snakemake is readable and has [extensive documentation already](https://snakemake.readthedocs.io/en/stable/). This makes your work reproducible. 

# My take on Snakemake 

## Setup
[Snakemake](https://snakemake.readthedocs.io/en/stable/) already has a great introduction and well-written documentation set up, so look there for a basic "hello world" like experience. 
After you understand the basic mechanics, there tips might make more sense. 

[Syntax highlighting](https://snakemake.readthedocs.io/en/stable/project_info/faq.html?highlight=syntax%20highlighting#how-do-i-enable-syntax-highlighting-in-vim-for-snakefiles) is one of the first things to do.

Then, I organize the work directory into `snakes`, `scripts`, and `raw`, which are for the auxiliary snake files, the script for performing tasks (nodes in the workflow), and the raw results.  There's also a script for collecting `raw` into a database, which is usually stored in a fourth directory, `data`. 

The main `Snakefile` contains the helper functions and imports required, and contains the `rule`s used for submitting jobs, [described here](#running-rules). It imports all the Snakemake scripts in `snakes`, which are all the `rule`s that are nodes of the workflow.

## Directory structure
Inside `raw` I try to organize the directories by dependencies. If any run depends at all on a previous step, it appears as a subdirectory of that one. Try to limit these dependencies as much as possible, e.g. if there are many parameters to scan over, they all are given side-by-side directories in one directory. Keep the directory tree as wide as possible, because the wider it is, the more jobs can run in parallel. If a job actually uses the output of another job _only then_ should it be in a subdirectory. 

The goal of this organization is so that archiving or deleting runs will automatically archive or delete all runs that depended on that run. If jobs have multiple dependencies, things get tricky, and where it should go has to be evaluated on a case-by-case basis. [An example is below](#example-snakemake-rule). If you can't figure out a good way to do this it isn't a big problem, because Snakemake will rerun jobs that depend on files that have changed, and doesn't require this structure in any way.

## Writing rules
Start by making a `rule` for any step of your workflow that takes more than a few seconds to execute.  The rule will consist of `input`, `output`, `params`, and `run` sections. 

Stay as honest as possible when choosing the `input` and `output` files for the step.  I experimented with having auxiliary files as `input` or `output` members, but it was a disaster, because, in short, they need to be kept synchronized with the "real" input and output files.  Having a dynamic `output` or wanting to save `output` from crashed runs is [dicussed below](#tricks-for-tricky-situations). Keep STDOUT and STDERR from the run out of the `output` section if possible, because `output` gets deleted if the jobs crash.

In `params`, I like to always have at least two members, the run location, and the job parameter specification that will be written to disk for the submission, as described next. 

In `run`, I always write the specific job parameters to JSON on disk in the run location, and submit the job. Writing the run parameters to disk is great for record-keeping and makes submitting it as batch easier.  The job submission is done by copying the script from `scripts` to that directory and submitting a bash script which runs it. Copying the script preserves a record of the script that was run, and avoids problems where I may be editing that script when a batch job starts, and it uses the script in the middle of an edit. By copying that script, I'm sure that it's running the version that I had at the time of submission. 

## Running rules

You can make a `rule` with only input files and call `snakemake [rule]` to generate those input files. 

For quick, on-the-fly snakemake calls, you can use the `bash` syntax for generating combinations of file names like this:
```
snakemake raw/test_{0,1,2}_param{0.3,0.4,0.5}/doit.py`
```
Which automatically generates all combinations of the lists provided. If you want to avoid taking cartesian products, you'd best go back to making small custom rules. 

## Example snakemake rule

Wildcards in the same file name are in some sense parallel, and don't depend on one another. From the `input` you can see that parent directories contain `input` files.
```
def jsondump(data,loc):
  with open(loc,'w') as outf:
    json.dump(data,outf,indent='  ')

def subscript(fn,loc,**subargs):
  shutil.copy(f"scripts/{fn}",f"{loc}/{fn}")
  cwd = getcwd()
  chdir(loc)
  subpy(fn, **subargs)
  chdir(cwd)

BIGPYSUB = {'wait':True, 'extra_mods':['bndefect'], 'ptype': 'rome'}

freezestr = "{pyloc}/{dscfloc}/{basloc}/fr{state}_svd{svdtol}_pm{pmtol}_reopt{reopt_tol}"
rule freeze_ham:
  input:
    chk    = "{pyloc}/pycalc.chk",
    gdf    = "{pyloc}/pycalc_gdf.h5",
    basis  = "{pyloc}/{dscfloc}/{basloc}/basis_{state}.h5",
  output:
    ham   = freezestr + "/ham.h5",
    info  = freezestr + "/freezeinfo.h5",
  params:
    loc   = freezestr, 
    json  = freezestr + "/ham.in.json",
  run:
    jsondump(dict(
        chk         = relpath(input['chk'], params['loc']),
        gdf         = relpath(input['gdf'], params['loc']),
        basis       = relpath(input['basis'], params['loc']),
        svdtol      = float(wildcards.svdtol),
        occtol_svd  = float(wildcards.pmtol),
        reopt_tol   = float(wildcards.reopt_tol),
        state       = int(wildcards.state),
      ),params['json'])
 
    subscript("freeze_ham.py",params['loc'],time='2-0',**BIGPYSUB)
```

# Tricks for tricky situations

## Dynamical output files

Snakemake allows you to dynamically change input files by creating a function that generates the list of input files. I had an example of this somewhere which I can't find, but I'll try to add it later. It doesn't let you do the same for output files. I'm guessing this is because it cannot tell if a `rule` can produce the output you want until it is being run. 

Instead you have to use an auxiliary file to represent the dynamically-generated list of output files that you want. For example, you can create a JSON file that has a list of the files generated. The downside of this is that you need to take care that any changes to the output files are reflected in the auxiliary file. For example, if the output files get changed by an external script, Snakemake will not know unless you update the auxiliary file, and so safeguards that Snakemake uses to ensure that the runs are consistent with the workflow description won't be activated. 

## Stop deleting my output if the run crashes!

Snakemake deletes output from crashed or incomplete runs in order to avoid accidentally saving corrupt output files and thinking they are complete. For this reason, try to keep the raw results seperate from where the STDOUT and especially the STDERR gets placed, and keep those files out of the `output` section. 

Sometimes true data output files are useful even if the job is crashed. For example, PySCF runs a calculation which produces a `chkfile`, which contains the intermediate and eventually the final solution to a system of differential equations. If the job crashes, the intermediate results are useful for diagnosing and restarting. The solution is to keep the file name for the intermediate results separate from the final results. I like to issue a `move` command at the end of my PySCF script to rename to file from it's intermediate name to a final name, signifying completion. 

## Why is snakemake trying to run files that are already there?

Snakemake will rerun a job if any of its `output` is older than its `input`. Sometimes you accidentally modify a file's last modification time, and it causes Snakemake to want to rerun a bunch of jobs. If you want to reset all the file's modification times to prevent this, run `snakemake --touch -j1`. If a file doesn't exist when you run this, it will simply pass over it as if the blood of the lamb was on the doorframe.

## Ambiguities in rule preference

The easiest solution is to use [the `ruleorder` section](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#handling-ambiguous-rules). You can also use [constraints](https://snakemake.readthedocs.io/en/stable/tutorial/additional_features.html#constraining-wildcards), but the regex syntax is not defined anywhere, so I always have trouble using it.

