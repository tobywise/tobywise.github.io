---
title:  "Making science with neural networks"
date:   2017-08-09 15:00:00
tags: [blog, neural networks]
image: img/img.png
---

As scientists, our primary aim is to publish papers in flashy journals such as Nature and Science (despite some claims that we should instead be focusing on extending human knowledge). In service of this aim, we spend immeasurable numbers of hours attempting to devise novel and exciting experiments that will seduce the editors of such journals and enable us to further our careers.

However, this seems a little inefficient. What if we could instead generate experiments that would be worthy of publication in these top journals instantly and automatically, leaving us to then simply carry out the work safe in the knowledge that the results would be gauranteed to appear in a top-tier publication?

I've recently seen many great (and hilarious) examples of neural networks being used to generate samples of text based on training datasets (http://lewisandquark.tumblr.com/ is worth spending several hours reading - she's used neural networks to generate beer names, recipes, and name cats), and thought this seemed the ideal solution to this problem - can we generate ideas for papers with this new technology?

To try this out I retrieved titles of the most recent 50,000 papers published in Nature and Science, and set to work. I used a Python implementation of a char-rnn, based on Theano and Lasagne (I admit I did this half because I found the idea of writing `import lasagne` amusing), and trained it on these paper titles. After about 15 hours, it seemed to have a pretty good understanding of the entirity of science, and was producing some exciting, often strikingly inter-disciplinary, papers of its own.

* The structure of the human gut microbiome in the solar system.
* An extremely layer regulates biodiversity and the evolution of forest coupling at the centre of the global carbon cycle.
* The genomic landscape of the electron pairing between the evolution of the southern ocean carbon nanotubes.
* The genome of the supermassive black hole in an early mammals.
* Antibody-mediated spindle of a single atoms in the tropical forest haematopoietic stem cell division in a compact density wave in the solar system.
* Complexity of complex communities.
* Structural basis for the control of protein activity in macaques.
* Activation of the endoplasmic reticulum stress in the hippocampus.
* A microbial genetic discovery of a protein phosphatase 2A and implications for the continental graphene transition.
* A high-resolution structure of the Amazon deforestation and antibiotic resistance in the solar system.
* A massive star formation in the abundant microbiota.
* A progressive insight into the adult neural selection in a mouse model of the human genome.
* Reconstructing the genome sequence of an extrasolar planet.
* A resonant liquid from the leaving circulating wave revealed by self-renewing infective reactivity and temporal diversity in a stripped-resourcting the histone modification enhances neural responses to climate change.
* A strong magnetic field in the hippocampus.
* An atomic methanol using CO-methylatropospheric during the last deglaciation.
* Antidepressants in a global clouds from modern human impacts on molecular channels.
* Plant invasion by a radical proteome.
* The missing memory in an exceptional patterns in metallic glasses.
* A general model of the surface of the Southern Ocean deep states by means of interaction with neurotransmitter release.
* A gene regulatory network states in a superconducting qubits via atomic clock on the contributor of a potassium channel Ca(2+) and PAL1 and toxicity in a tropical forests.
* Discovery of a three-dimensional transition in the face of rapid warming leads to collapse of the Sun.
* Complex carbon nanotubes in medial prefrontal cortex.
* Complex structure of a metatherically stabilized reconstructed by massive mice.

It had even learnt that it was possible to write commentaries (it's interesting to think about the thoughts such a commentary would contain given the subjects of these papers...):

* Comment on "A common genetic variants associated with a single component of the mitochondrial calcium uniporter.
* Comment on "A common genetic variants in the developmental disorder in the active site of the tropical Antarctic ice sheet.
* Comment on "Density using mitochondrial fibroblastoma stemplling by the supersout restore responses in metal organic matter to ecosystems.

Some are even somewhat believable, if a little vague:

* Control of the human transcriptome.
* The structure of the human gut microbiome composition and its regulation.
* Structure of the mammalian circadian clock.
* Rapid early microscopic observation of inflammation.
* Suppression of the southern ocean acidification.

It's interesting that the neural network appears to believe certain phrases are particularly important to science today; genetic variants, structures, cirdadian clocks, and the southern ocean are frequently mentioned.

In summary, this has worked flawlessly and I will now be radically changing my research direction to focus on understanding complex carbon nanotubes in the medial prefrontal cortex. Expect to the see the results published in Nature soon.