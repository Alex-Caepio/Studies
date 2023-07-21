dna = 'GTAT'

dna_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}


def DNA_strand(dna):
    result_strand = ''
    for letter in dna:
        pair_letter = dna_dict.get(letter, 0)
        if pair_letter != 0:
            pair_letter = dna_dict[letter]
            result_strand += pair_letter
    return result_strand


print(DNA_strand(dna))
