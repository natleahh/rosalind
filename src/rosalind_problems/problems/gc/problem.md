
> Identifying Unknown DNA Quickly
> -------------------------------
> 
> [![](https://rosalind.info/media/problems/gc/English_letter_frequency.thumb.png)](https://rosalind.info/media/problems/gc/English_letter_frequency.png)**Figure 1**. The table above was computed from a large number of English words and shows for any letter the frequency with which it appears in those words. These frequencies can be used to reliably identify a piece of English text and differentiate it from that of another language. Taken from http://en.wikipedia.org/wiki/File:English\_letter\_frequency\_(frequency).svg.A quick method used by early computer software to determine the language of a given piece of text
> was to analyze the frequency with which each letter appeared in the text. This strategy was used because each language
> tends to exhibit its own letter frequencies, and as long as the text under consideration is long enough,
> software will correctly recognize the language quickly and with a very low error rate.
> See [Figure 1](/media/problems/gc/English_letter_frequency.png "Click to view")for a table compiling English letter frequencies.
> 
> You may ask: what in the world does this linguistic problem have to do with biology?
> Although two members of the same species will have different [genomes](/glossary/genome/ "
> The collection of all of an organism's DNA taken from all its chromosomes."), they still share
> the vast percentage of their [DNA](/glossary/dna/ "
> The molecule encoding heredity and underlying the cellular processes of all life forms."); notably, 99\.9% of the 3\.2 billion [base pairs](/glossary/base-pair/ "
> The combination of two bonded complementary bases.")in a human genome are common to almost all humans (i.e., excluding people having
> major genetic defects). For this reason, biologists will speak of *the* human genome, meaning an average\-case
> genome derived from a collection of individuals. Such an average case genome
> can be assembled for any species, a challenge that we will soon discuss.
> 
> The biological analog of identifying unknown text arises
> when researchers encounter a molecule of DNA from an unknown species.
> Because of the base pairing relations of the two DNA [strands](/glossary/strand/ "
> A nucleic acid polymer."), cytosine and guanine
> will always appear in equal amounts in a double\-stranded DNA molecule.
> Thus, to analyze the symbol frequencies of DNA for comparison against a database, we compute the
> molecule's [GC\-content](/glossary/gc-content/ "New term: 
> The percentage of cytosine and guanine bases in a strand of nucleic acid."), or the percentage of its [bases](/glossary/nucleobase/ "
> The differentiating component of nucleotides.") that are *either* [cytosine](/glossary/cytosine/ "
> One of the nucleobases of both RNA and DNA; complementary to guanine.") or [guanine](/glossary/guanine/ "
> One of the nucleobases of both RNA and DNA; complementary to cytosine in DNA.").
> 
> In practice, the GC\-content of most [eukaryotic](/glossary/eukaryote/ "
> Eukaryotes form the most complex domain of life, which includes all multicellular organisms.") genomes hovers around 50%. However, because
> genomes are so long, we may be able to distinguish species based on very small discrepancies
> in GC\-content; furthermore, most [prokaryotes](/glossary/prokaryote/ "
> A bacterial organism.") have a GC\-content significantly higher than 50%,
> so that GC\-content can be used to quickly differentiate many prokaryotes and eukaryotes by using relatively small DNA samples.

Problem
-------

The GC\-content of a [DNA string](/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") is given by the percentage of [symbols](/glossary/symbol/ "
The constituent individual elements of a string, which may constitute numbers and letters.") in the string that are 'C' or 'G'.
For example, the GC\-content of "AGCTATAG" is 37\.5%.
Note that the [reverse complement](/glossary/reverse-complement/ "
The DNA string formed by reversing and complementing each symbol.") of any DNA string has the same GC\-content. 

DNA strings must be labeled when they are consolidated into a database. 
A commonly used method of string labeling is called [FASTA format](/glossary/fasta-format/ "New term: 
A text format used for naming genetic strings in databases."). In this format, the string is
introduced by a line that begins with '\>', followed by some labeling information.
Subsequent lines contain the string itself; the first line to begin
with '\>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID
"Rosalind\_xxxx", where "xxxx" denotes a four\-digit code between 0000 and 9999\.

Given: At most 10 [DNA strings](/glossary/dna-string/ "
A string constructed from the alphabet {A, C, G, T}.") in FASTA format (of length at most 1 [kbp](/glossary/kbp/ "
1 kbp = 1000 base pairs") each).

Return: The ID of the string having the highest GC\-content, followed by the GC\-content of that string.
Rosalind allows for a default error of 0\.001 in all decimal answers unless otherwise
stated; please see the note on [absolute error](/glossary/absolute-error/ "New term: A measure of how close a computed value is to a correct solution.") below.

Sample Dataset
--------------

```
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

```

Sample Output
-------------

```
Rosalind_0808
60.919540

```

> Note on Absolute Error
> ----------------------
> 
> We say that a number $x$ is within an absolute error of $y$ to a correct solution if $x$is within $y$ of the correct solution. For example, if an exact solution is 6\.157892,
> then for $x$ to be within an absolute error of 0\.001, we must have that $\|x \- 6\.157892\| \< 0\.001$,
> or $6\.156892 \< x \< 6\.158892$.
> 
> Error bounding is a vital practical tool because of the inherent round\-off error in representing
> decimals in a computer, where only a finite number of decimal places are allotted to any number.
> After being compounded over a number of operations, this round\-off error can become evident.
> As a result, rather than testing whether two numbers are equal with $x \= z$, you may
> wish to simply verify that $\|x\- z\|$ is very small.
> 
> The mathematical field of [numerical analysis](/glossary/numerical-analysis/ "New term: 
> The mathematical study of computational approximation.") is devoted to rigorously studying
> the nature of computational approximation.

