--- 
layout: page
title: Using ppconvert from QMCPACK
category: notes
tags: [physics,research,code,tools]
excerpt: How to convert a pseudopotential format using ppconvert.
---

Some [basic documentation]({{ "https://code.google.com/archive/p/qmcpack/wikis/ppconvert.wiki" }}) already exists on the web, but there were some tricks that [Paul]({{ "http://publish.illinois.edu/yubo-paul-yang" }}) told me and saved me many hours of fiddling.

My task was to covert a Si pseudopotential from the [BFD web site]({{"http://www.burkatzki.com/pseudos/index.2.html"}}) to a format that can be read in by Quantum Espresso. 

## Getting your hands on `ppconvert`.
[QMCPACK]({{ "https://github.com/qmcpack" }}) is an open-source quantum Monte Carlo code that does *many* things, but among them is a converter for pseudopotentials.
The converter lives in `qmcpack/src/QMCTools/ppconvert/` where there is a `README` with compile instructions.
You execute those compile instructions in the `qmcpack/build/` directory (from the QMCPACK root).

## Using `ppconvert` for Si.
Once that is done, the `ppconvert` executable exists in the `qmcpack/build/bin`. 
Copy the pseudopotential section from the BFD web page into a text file, I called it `./bfd`. 
Then I executed the following command:

    ppconvert --gamess_pot bfd --s_ref "1s(2)2p(2)" --p_ref "1s(2)2p(2)" --d_ref "1s(2)2p(2)" --upf bfd_si.upf

Breaking this down: 

* I copied the GAMESS input format for Si, so thats what `--gamess_pot` is all about.
* `--s_ref` etc. is the valence state in a funky format. The preceding number seems to be iterating across angular momentum channels. Paul suggested doing all of the valence state for each channel, but I suspect it ignores the "s" part for the `--p_ref`, for instance.
* `--upf` specifies the output format. The last thing is the resulting output that I wanted.

The process utilizes the Kleinman-Bylander approximation, and I believe it performs an LDA on the pseudoatom system to figure out if the potentials match.
I think the correspondence between ground-state densities and potentials is the theoretical grounding for this. 

## Checking the conversion.

Will be added shortly...

