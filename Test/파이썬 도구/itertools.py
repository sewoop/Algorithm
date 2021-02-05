from itertools import product, permutations, combinations, combinations_with_replacement

# MARK: Product
product = product('ABCD', repeat=2) # 결과: AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

# MARK: Permutations
permutations = permutations('ABCD', 2) # 결과: AB AC AD BA BC BD CA CB CD DA DB DC

# MARK: Combinations
combinations = combinations('ABCD', 2) # 결과: AB AC AD BC BD CD

# MARK: Combinations with replacement
combinationsWithReplacement = combinations_with_replacement('ABCD', 2) # 결과: AA AB AC AD BB BC BD CC CD DD
