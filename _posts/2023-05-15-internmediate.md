---
layout: single
title: "Internmediate"
date: 2023-05-15 00:01:01 -04:00
author_profile: true
header: 
  image: assets/images/hasan-almasi.jpg
  teaser: assets/images/teasers/hasan-almasi.jpg
  caption: "Photo credit: [Hasan Almasi](https://unsplash.com/photos/rRTtg-jTQ_s)" 
toc: true
toc_sticky: true
categories: [Internship, Research, Games]
---

"The best teaching can be done only when there is a direct individual relationship between a student and a good teacher." — Richard Feynman, Foreword of *The Feynman Lectures on Physics*, Volume I

## Sudoku
I have been quite obsessed with Sudoku recently, playing evil mode on [Sudoku.com](https://sudoku.com) until 2 AM. 

### Tips?
There are some techniques which I did not immediately recognize, but could figure out, and some techniques that I only learned through looking them up. 

I prefer to use simple elimination rather than tedious tricks like X-wing or chaining. Sometimes, to do these techniques, every possible location of the numbers needs to be written down. 

Normally, I will only take note of where a number can be in a square if there are 2 or 3 places that it can be. 

I feel that I lack a sense of how the other values in the smaller boxes can be used in combination with the values of rows and cols. 

I usually just resort to going through 1-9 and looking for linear possibilities down the rows and cols. This allows me to note the locations of populous numbers, but not sparse ones. 

For sparse numbers, it is usually possible to eliminate **other** numbers from a square so that the only possibility is the sparse value. This usually leads to a firework of other possibilities, which allows me to return to scanning for linear possibilities. 

## Antibody-Antigen Interactions Research Internship
The goal of my reserach is to create a machine learning model capable of telling whether any antibody (Ab) will bind to any antigen (Ag). 

### Proteins
Proteins are the building blocks of life, which can also be said for DNA, but DNA is more like the blueprint, whereas protein is more like the car. 

Each protein is made of chains of amino acids/residues in a 3-D structure. Each residue is made of a couple atoms, like carbon and oxygen. By using imaging techniques which are not important to my project, each protein's chains's amino acids's and atoms's locations are recorded in a PDB (Protein Data Bank) file. 

Note: according to *Strunk and White*, possessive of a plural is adding the 's after the plural; e.g., atoms's.

### Ab and Ag binding
In medicine, Ab is the drug molecule and Ag is the virus. Using COVID as an example, the vaccine would be the Ab and the Ag could be the coronavirus spike protein or another protein of the virus. 

The way that Ab drugs usually work is by binding to the Ag, and that will cause the virus to lose some of its functionality because it is being **inhibited** or dragged down in a structural way (kind of like when someone holds your leg so you cant walk, but it is not necessarily based on increasing mass). 

When two residues are close together, they can be considered interacting with each other. There may be a correlation found between whether a combination of Ab and Ag will interact and a count of the types of combinations of interactions between an Ab and Ag. For example, a higher concentration of the Alanine-Glycine interaction, might mean a greater chance of interaction.

### Counting
the interactions is very annoying, since it uses a very slow complete search algorithm. However, at least it is simple and could not go wrong. 

As an exercise to the reader, if there are only two chains (Ab and Ag respectively) in a single PDB file, and each of the 2N residues (combined) of the two chains has an average location recorded, what would be the big-O time complexity of the complete position closeness search?

### Intra-Ab/Ag interactions
I will use a program to record the interacting residues in the Ag and Ab and then record their internal interactions with themselves (I call it an intra-Ab/Ag interaction). 

You may be wondering, why use intra-Ab/Ag interactions rather than the direct interaction pairs? Well, if you were to test a new type of vaccine on COVID, for example, then you wouldn't know where the interaction would happen exactly. Not to mention that you wouldn't even know if it would bind at all. However, the interacting region in the Ag remains constant.

Now you may be wondering, well, wouldn't you also not know where the interaction of the Ab is? In that case, it is known that a special area inside the Ab protein, the complementarity-determining region (CDR) can be used to roughly approximate the effect of the protein. 

EDIT 1: For the Ag protein, it is possible to use software such as Schrodinger's SiteMap in order to find the likely binding sites.  

As an example of counting interactions, if residues A, B, C in Ag interact with residues D, E, F in Ab, then I will try to see if A, B, C interacts with each other. These intra-Ag interaction combinations can be recorded in a 20 by 20 heatmap/table of the 20 types of amino acids. I would repeat the same process for the Ab except toss out D, E, F in favor of CDR region which has a numerically similar range of rows in the PDB file. 

Afterward, we will end up with two symmetrical heatmaps for the Ab and Ag, respectively, of a single PDB file. 

### Machine learning and CNN
Now, with thousands of heatmaps available, we can first cut every heatmap in half to be left with a bunch of 20 by 20 triangular heatmaps. Then, we can mix the matches of the triangles so that there are a set of actually interacting pairs of Ab and Ag (the original PDB files), as well as a set of randomly matched triangles. It is assumed that the random pairs will not interact.

Now, we have a dataset of valid and invalid pairs in the form of 20 by 21 images (it will be an exercise to the reader as to why it is 20 by 21 instead of 20 by 20), and can train a CNN to predict whether an image is valid or invalid. 

Hopefully, the CNN will actually have some reasonable accuracy after 10-fold cross-validation. 

EDIT 2: The project is going much more smoothly than expected, but the design and creation of the heatmap is quite a puzzle. The main issue is, if I loop through the residues and look for interactions, I will be counting interactions of the same type in two ways. For example, if I had many Alanine (A) and Proline (P) interactions, they would be recorded as both A-P and P-A. On the heatmap, those correspond to two different halves of the heatmap which must be condensed down to a single triangle. So, only a single organization can exist.

EDIT 2, cont.: I think lexicographically ascending (alphabetical order) would work well. However, I either convert every P-A to an A-P during the adding to the dictionary or I just do that after the code runs. They both take roughly the same computation time (fast), but I would prefer to not need to sort everything out at the end since I would need to search every possible combination of amino acids and then modify the dictionary's values; however, by changing the order immediately after finding the combination, it is a simple comparison, and then I can add the correct combination to the dictionary. 