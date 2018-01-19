from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='nucompress',
      version='0.1',
      author='Jordan Gumm',
      description='Nucleotide Compression Library',
      author_email='gumm@umich.edu',
      packages=['nucompress'],
     )
