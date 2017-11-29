# nucompress
A python library for dynamic genomic sequence compression.  More specifically, it provides implementations of lossless without reference genomes.

## 2-bit encoding
The simplest compression method for DNA sequences, four nucleotides are packed into a single byte.

Usage:

We can encode any nucleotide sequence into a encoded string.  Each nucleotide is converted to a 2-bit representation, meaning every 4 nucleotides can fit into a byte/char.
```python
>>> from nucompress.compression import TwoBitCompression
>>> compressor = TwoBitCompression()
>>> seq = 'CTGACTGGCTGACTGG'
>>> encoded_seq = compressor.encode_nuc(seq)
>>> encoded_seq
{'length': 16, 'seq': 'xzxz'}
```

The encoded sequence can then be decoded back to its original nucleotide sequence.  This basic encoding process gives roughly a 4x compression rate with no loss of data (outside of possible N values).
```python
>>> decoded_seq = compressor.decode_nuc(encoded_seq['seq'],
                                        encoded_seq['length'])
>>> decoded_seq
'CTGACTGGAA'

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
