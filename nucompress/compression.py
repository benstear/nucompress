from nucutil import split


class TwoBitCompression(object):
    """ Nucleotide to 2-bit representation to 4-nuc per byte/char compression """

    def __init__(self):
        self.mappings = mappings = {'A': '00', '00': 'A',
                                    'C': '01', '01': 'C',
                                    'G': '10', '10': 'G',
                                    'T': '11', '11': 'T'}

    def encode_nuc(self, seq):
        """ Maps nucleotide string to 4x smaller bytechar representation """
        seq = seq.replace('N','')
        encoded_string = ''
        for kmer in split(seq, 4):
            while len(kmer) < 4: kmer = '{}A'.format(kmer) # fill in last kmer to full byte
            binary_string = ''
            for bp in kmer:
                binary_string += self.mappings[bp]
            encoded_string += chr(int(binary_string, 2))
        return {'seq':encoded_string,'length':len(seq)}

    def decode_nuc(self, encoded_seq, length):
        """ Maps bytechar string to nucleotide string """
        seq = ''
        for c in encoded_seq:
            binary_string = '{0:08b}'.format(ord(c))
            while len(binary_string) < 8: binary_string = '0{}'.format(binary_string) # fill in binary string to full byte
            for bp in split(binary_string, 2):
                seq += self.mappings[bp]
                if len(seq) == length:
                    break # escape if length of original sequence is met, avoiding extended A encoding (see above)
        return seq
