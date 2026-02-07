class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0      # number of 'b's seen so far
        deletions = 0    # minimum deletions so far

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                deletions = min(
                    deletions + 1,  # delete this 'a'
                    b_count         # delete all previous 'b's
                )

        return deletions
