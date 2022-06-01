# Genetic Algorithm simple Program
creation of a simple program that uses the evolutionary methods to generate a pre determined solution, in our case it being a simple sentence from shakespeare's
work i.e. to generate a sentence "to be or not to be."

This is a simple implementation of the solution to the "infinite monkey theorem" that is being discussed in chapter 9 of Nature of Code book by Daniel Shiffman. so the theorem is stated as follows : a monkey will eventually produce shakespeare work given it is provided infinite time. The actual probability of this being true is so low that if we assume the monkey starts banging the keyboard at the begining of big bang it is highly unlikely that he prints out the "Hamlet".

To illustrate Daniel's point: Assume we ask the monkey to type out "to be or not to be.", it consists of 19 characters and the probability of him coming up with this answer is 1 in 19^26. Our code is going to simulate such generations of monkey families that starts simply by banging on the keyboard and continue until one smart monkey types out this whole sentence correctly hence satisfying our requirement.
