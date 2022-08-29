--- 
layout: page
title: Reduced density matrix
category: notes
tags: [math,physics,operators,density matrix,coarse graining,Koopman's theorem]
excerpt: The reduced density matrix is a tool for analyzing the many-body wave function in terms of one-body, two-body, and other lower-body operators.
---

The one-body reduced density matrix can be succinctly represented as 
$$
\langle \Psi | c_i^\dagger c_j | \Psi \rangle.
$$
Its diagonal is simply the density of electrons. 
Its off-diagonal represents a measure of the correlation between the occupation of two single-particle orbitals.
This is often interpreted as "hopping" (although there is no dynamical aspect to it) because large elements between two atoms implies there is bonding between those atoms.
A tight binding model is a model that is expressed in terms of the one-body density matrix.

The two body density matrix,
$$
\langle \Psi | c_i^\dagger c_k^\dagger c_j c_l | \Psi \rangle,
$$
can represent correlations in electron density (like Hubbard-interactions), as well as other correlations. 

[These notes]({{ "/assets/pdfs/density_matrices.pdf" }}) discuss the construction and interpretation of the density matrix, and some nice tricks you can do with them.
