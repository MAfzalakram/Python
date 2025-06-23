import copy
original_list = [1, 2, [3, 4]]
alias_list = copy.deepcopy(original_list) # This is NOT a copy

print(f"Original ID: {id(original_list)}")
print(f"Alias ID:    {id(alias_list)}") # Same ID

alias_list.append(5)
print(f"Original after alias modification: {original_list}") # original_list is also modified
# Output: Original after alias modification: [1, 2, [3, 4], 5]

alias_list[2][0] = 99
print(f"Original after alias nested modification: {original_list}") # original_list is also modified
# Output: Original after alias nested modification: [1, 2, [99, 4], 5]
print(f"Original after alias nested modification: {alias_list}") # original_list is also modified
# Output: Original after alias nested modification: [1, 2, [99, 4], 5]