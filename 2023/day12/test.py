def generate_permutations(s, index=0):
    if index == len(s):
        return [s]
    
    permutations = []
    if s[index] == '?':
        # Replace with '#' and generate further permutations
        permutations.extend(generate_permutations(s[:index] + '#' + s[index + 1:], index + 1))
        # Replace with '.' and generate further permutations
        permutations.extend(generate_permutations(s[:index] + '.' + s[index + 1:], index + 1))
    else:
        permutations.extend(generate_permutations(s, index + 1))

    return permutations

# Initial string with '?'
initial_string = "?###????????"
# Generating permutations
permutations = generate_permutations(initial_string)
print(permutations[:10], len(permutations) )