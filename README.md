# nucompress
A python library for genomic sequence compression.  It provides implementations of lossless without reference schemes.

## 2-bit encoding
The simplest compression method for DNA sequences, four nucleotides groups are packed into single unicode characters (8-bit bytes).  This basic encoding process gives roughly a 4x compression rate with no loss of data outside of possible N values, which it removes to preserve the possibility of 2-bit encoding.

Usage:

A nucleotide sequence can be encoded via a series of 2-bit mappings, with 8-bit binary strings being converted to unicode characters.
```python
>>> from nucompress.compression import TwoBitCompression
>>> compressor = TwoBitCompression()
>>> seq = 'CTGACTGGCTGACTGG'
>>> encoded_seq = compressor.encode_nuc(seq)
>>> encoded_seq
{'length': 16, 'seq': 'xzxz'}
```

The encoded sequence can then be decoded back to its original nucleotide sequence.
```python
>>> decoded_seq = compressor.decode_nuc(encoded_seq['seq'],
                                        encoded_seq['length'])
>>> decoded_seq
'CTGACTGGCTGACTGG'

>>> len(encoded_seq['seq'])
4
>>>len(decoded_seq)
16
```

## Installation

You can do:
```pip install -e git+https://github.com/jordangumm/nucompress.git#egg=nucompress```

nucompress was built and tested under Python 2.7.x

## Support

Please ask questions and file issues [on Github](https://github.com/jordangumm/nucompress/issues).
