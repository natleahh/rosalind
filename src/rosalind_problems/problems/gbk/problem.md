
> The World's Biggest Genetic Database
> ------------------------------------
> 
> The most comprehensive database available for molecular biologists is [GenBank](/glossary/genbank/ "New term: 
> The world's largest genetic database, hosted by NCBI"), an open access resource that contains
> an annotated collection of all publicly available [sequenced](/glossary/genome-sequencing/ "
> Determining the entire genome of an organism.") [DNA](/glossary/dna/ "
> The molecule encoding heredity and underlying the cellular processes of all life forms.") and its [translation](/glossary/translation/ "
> The process by which mRNA is converted into a peptide chain for the creation of a protein.") into [proteins](/glossary/protein/ "The functional unit of the cell.").
> GenBank was founded by [NCBI](/glossary/national-center-for-biotechnology-information/ "
> A branch of the NIH that offers a collection of genetic databases, including GenBank.") in 1982, and over the last three decades, the data it houses has grown exponentially,
> doubling every 18 months. As of August 2012, GenBank contained over 143 **billion** [nucleobases](/glossary/nucleobase/ "
> The differentiating component of nucleotides.").
> 
> Every sequence has a unique GenBank identifier that will directly retrieve 
> its full sequence record. Here are some examples of database IDs:
> 
> 
> ```
>  CAA79696
>  NP_778203
>  263191547
>  BC043443
>  NM_002020
> ```
> 
> 
> You can also search by submitter/author name in the format `last_name first_initials` (e.g., `Smith JR`). 
> 
> To search for an exact match, enclose it in quotation marks.
> 
> 
> ```
> "contactin associated protein"
> "duchenne muscular dystrophy"
> ```
> 
> 
> You can also restrict your search by using Boolean operators (AND, OR, NOT) as well as
> use specific subsets of records.

Problem
-------

GenBank comprises several subdivisions:

* [Nucleotide](http://www.ncbi.nlm.nih.gov/nucleotide): a collection of [nucleic acid](/glossary/nucleic-acid/ "
A polymer of nucleotides, constituting either RNA or DNA.") [sequences](/glossary/genetic-string/ "
A DNA, RNA, or amino acid string.") from several sources.
* [Genome Survey Sequence](http://www.ncbi.nlm.nih.gov/gss) (GSS): uncharacterized short [genomic](/glossary/genome/ "
The collection of all of an organism's DNA taken from all its chromosomes.") sequences.
* [Expressed Sequence Tags](https://www.ncbi.nlm.nih.gov/est), (EST): uncharacterized short [cDNA](/glossary/complementary-dna/ "
DNA created by reverse transcription from mRNA.") sequences.

Searching the Nucleotide database with general text queries will produce the most relevant results.
You can also use a simple query based on protein name, gene name or [gene symbol](/glossary/gene-symbol/ "
A short-form abbreviation for a gene.").

To limit your search to only certain kinds of records, you can search using GenBank's [Limits](http://www.ncbi.nlm.nih.gov/nuccore/limits) page or alternatively use the `Filter your results` field to select categories of records after a search.

If you cannot find what you are searching for, check how the database interpreted your query
by investigating the `Search details` field on the right side of the page.
This field automatically translates your search into standard keywords.

For example, if you search for `Drosophila`, the `Search details` field will contain (`Drosophila[All Fields]`), and you will
obtain all entries that mention *Drosophila* (including all its [endosymbionts](/glossary/endosymbiont/ "
An organism that lives within the body of another organism.")).
You can restrict your search to only organisms belonging to the *Drosophila* [genus](/glossary/genus/ "
A low-level taxonomical rank, one step above species.")by using a search tag and searching for `Drosophila[Organism]`.

Given: A [genus](/glossary/genus/ "
A low-level taxonomical rank, one step above species.") name, followed by two dates in YYYY/M/D format.

Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.

Sample Dataset
--------------

```
Anthoxanthum
2003/7/25
2005/12/27

```

Sample Output
-------------

```
7

```

> Programming Shortcut
> --------------------
> 
> NCBI's databases, such as [PubMed](/glossary/pubmed/ "
> A free international database of references and abstracts on life sciences topics."), GenBank, [GEO](http://www.ncbi.nlm.nih.gov/geo/),
> and many others, can be accessed via [Entrez](/glossary/entrez/ "
> A search engine that accesses multiple NCBI databases simultaneously."),
> a data retrieval system offered by NCBI. For direct access to Entrez, you can use [Biopython](/glossary/biopython/ "
> A collection of freely available tools for bioinformatics, written in Python.")’s `Bio.Entrez` module.
> 
> The `Bio.Entrez.esearch()` function will search any of the NCBI databases.
> This function takes the following arguments:
> 
> * `db` : The database to search. For example, this field can be `nucleotide` for GenBank or `pubmed` for PubMed.
> * `term`: The search term for the "Query" field. You can use search tags here.
> 
> We will now demonstrate a quick search for the rbcL gene in corn (*Zea mays*):
> 
> 
> ```
> >>>from Bio import Entrez
> >>>Entrez.email = "your_name@your_mail_server.com"
> >>>handle = Entrez.esearch(db="nucleotide", term='"Zea mays"[Organism] AND rbcL[Gene]')
> >>>record = Entrez.read(handle)
> >>>record["Count"]
> '6' # Surely this value will change over time because GenBank is constantly updated
> 
> ```
> Note that when you request Entrez databases you must obey [NCBI's requirements](http://www.ncbi.nlm.nih.gov/books/NBK25497/#chapter2.Usage_Guidelines_and_Requiremen):
> 
> * For any series of more than 100 requests, access the database on the weekend or outside peak times in the US.
> * Make no more than three requests every second.
> * Fill in the Entrez.email field so that NCBI can contact you if there is a problem.
> * Be sensible with your usage levels; if you want to download whole mammalian genomes, use NCBI's [FTP](http://www.ncbi.nlm.nih.gov/Ftp/).

