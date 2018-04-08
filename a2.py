def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    get_lenth = len(dna)
    return get_lenth

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if get_length(dna1) > get_length(dna2):
        is_longer = True
    else:
        is_longer = False
    return is_longer

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count_nucleotides = 0
    for char in dna:
        if char == nucleotide:
            count_nucleotides = count_nucleotides + 1
    return count_nucleotides

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    contains_sequence = False
    if dna1.find(dna2) != -1:
        contains_sequence = True
    return contains_sequence

def is_valid_sequence(dna):
    """ (str) -> bool
    Return True if and only if, dna contains no characters other than 'A', 'T', 'C' and 'G'.
    >>> is_valid_sequence('ATCGCTA')
    True
    >>> is_valid_sequence('GCTAB')
    False

    """
    is_valid_sequence = True
    for char in dna:
        if char not in 'ATCG':
            is_valid_sequence = False
    return is_valid_sequence

def insert_sequence(dna1,dna2,index):
    """
    (str,str,int) -> str
    The first two parameters are DNA sequences and the third parameter is an index. 
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence 
    at the given index. (You can assume that the index is valid.)
    >>> insert_sequence('CCGG','AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG','AT', 0)
    'ATCCGG'
    >>> insert_sequence('CCGG','AT', 3)
    'CCGATG'
    """
    insert_sequence = dna1[0:index] + dna2 + dna1[index:]
    return insert_sequence

def get_complement(nucleotide):
    """
    (str) -> str
    
    The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). 
    Return the nucleotide's complement. 

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    >>> get_complement('G')
    C

    """
    for char in nucleotide:
        if char == 'A':
            get_complement = 'T'
        elif char == 'T':
            get_complement = 'A'
        elif char == 'C':
            get_complement = 'G'
        else:
            get_complement = 'C'
    return get_complement

def get_complementary_sequence(dna):
    """
    (str) -> str

    The parameter is a DNA sequence. Return the DNA sequence that is complementary to the given DNA sequence. 
    For example, if you call this function with 'AT' as the argument, it should return 'TA'.
    
    >>> get_complementary_sequence('AT')
    TA
    >>> get_complementary_sequence('CG')
    GC
    >>> get_complementary_sequence('AGCTAC')
    TCGATG

    """
    get_complementary_sequence =''
    for char in dna:
        get_complementary_sequence = get_complementary_sequence + get_complement(char)
    return get_complementary_sequence






