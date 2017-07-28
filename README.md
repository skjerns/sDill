## sDill
A wrapper for dill to enable calls with filestrings

## Installation
`pip install git+https://github.com/skjerns/sDill`

## Usage
```Python 
import sdill
sdill.dump([1,2,3], 'filestr.pkl')
a = sdill.load('filestr.pkl')
print(a)
# [1,2,3]
```
