import unittest

from nucompress.compression import TwoBitCompression

class TestTwoBitCompression(unittest.TestCase):

    def test_basic(self):
        """ Test encoding/decoding against seq that fully fits into byte split

        Assert that decoded sequence is the same as original sequence
        Assert that encoded sequence is at least 4x shorter than original sequence
        """
        seq = 'ACGTACGT'
        compressor = TwoBitCompression()
        encoded_seq = compressor.encode_nuc(seq)
        decoded_seq = compressor.decode_nuc(encoded_seq['seq'], encoded_seq['length'])
        self.assertEqual(seq, decoded_seq)
        self.assertTrue(len(encoded_seq) <= len(seq))

    def test_offset(self):
        """ Test encoding/decoding against seq that doesn't fit fully into byte split

        Assert that decoded sequence is the same as original sequence
        Assert that encoded sequence is at least 4x shorter than original sequence
        """
        seq = 'CTGACTGGAA'
        compressor = TwoBitCompression()
        encoded_seq = compressor.encode_nuc(seq)
        decoded_seq = compressor.decode_nuc(encoded_seq['seq'], encoded_seq['length'])
        self.assertEqual(seq, decoded_seq)
        self.assertTrue(len(encoded_seq) <= len(seq))

    def test_N(self):
        """ Test encoding/decoding against seq that contains an N

        Assert that decoded sequence is the same as original sequence (minus Ns)
        Assert that encoded sequence is at least 4x shorter than original sequence
        """
        seq = 'ACGNTACNGT' # fits into byte split after N removal
        compressor = TwoBitCompression()
        encoded_seq = compressor.encode_nuc(seq)
        decoded_seq = compressor.decode_nuc(encoded_seq['seq'], encoded_seq['length'])
        self.assertEqual(seq.replace('N',''), decoded_seq)
        self.assertTrue(len(encoded_seq) <= len(seq))

        seq = 'CTGACNTGGNAA' # doesn't fit into byte split after N removal
        compressor = TwoBitCompression()
        encoded_seq = compressor.encode_nuc(seq)
        decoded_seq = compressor.decode_nuc(encoded_seq['seq'], encoded_seq['length'])
        self.assertEqual(seq.replace('N',''), decoded_seq)
        self.assertTrue(len(encoded_seq) <= len(seq))


if __name__ == '__main__':
    unittest.main()
