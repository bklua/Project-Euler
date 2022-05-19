

from functools import lru_cache

@lru_cache(maxsize=None)
def lattice_paths(m,n):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    
    return lattice_paths(m,n-1) + lattice_paths(m-1,n)
      
print(lattice_paths(21,21))
lattice_paths.cache_info()