    # Count the occurrences of each number in nums.
    for n in nums:
        count[n] += 1

    # Define a helper function to perform depth-first search (DFS) for generating permutations.
    def dfs():
        # Base case: If the temporary permutation is as long as the input list, add it to the result.
        if len(perm) == len(nums):
            res.append(perm.copy())  # Copy the temporary permutation to avoid modifying the result list.
            return

        # Iterate through each number that has not been used yet.
        for n in count:
            # Check if the current number has not been used in the current permutation.
            if count[n] > 0:
                perm.append(n)  # Add the current number to the temporary permutation.
                count[n] -= 1  # Decrement the count of the current number.

                # Recursively generate permutations starting from the current state.
                dfs()

                # Backtrack: Restore the count of the current number and remove it from the temporary permutation.
                count[n] += 1
                perm.pop()

    # Start the DFS to generate permutations.
    dfs()

    # Return the list of all unique permutations.
    return resa