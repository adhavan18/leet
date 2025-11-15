class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0
        
        # Precompute zero positions
        zero_pos = [i for i in range(n) if s[i] == '0']
        m = len(zero_pos)
        
        # For each starting position
        for i in range(n):
            # Binary search to find first zero >= i
            left = 0
            right = m
            while left < right:
                mid = (left + right) // 2
                if zero_pos[mid] < i:
                    left = mid + 1
                else:
                    right = mid
            
            zero_start = left
            
            # If no zeros from i onwards, all substrings are valid
            if zero_start >= m:
                result += n - i
                continue
            
            # Count substrings with 0 zeros
            result += zero_pos[zero_start] - i
            
            # Iterate through number of zeros (at most sqrt(n))
            max_zeros = min(int(n**0.5) + 1, m - zero_start)
            
            for k in range(max_zeros):
                if zero_start + k >= m:
                    break
                    
                # k+1 zeros in substring
                num_zeros = k + 1
                last_zero_idx = zero_start + k
                last_zero_pos = zero_pos[last_zero_idx]
                
                # Count ones from i to last_zero_pos
                substring_len = last_zero_pos - i + 1
                ones_count = substring_len - num_zeros
                
                # Need ones >= zeros^2
                required_ones = num_zeros * num_zeros
                
                if ones_count >= required_ones:
                    # Already satisfied at last_zero_pos
                    # Find next zero or end of string
                    if last_zero_idx + 1 < m:
                        next_zero = zero_pos[last_zero_idx + 1]
                    else:
                        next_zero = n
                    result += next_zero - last_zero_pos
                else:
                    # Need more ones after last zero
                    needed = required_ones - ones_count
                    
                    # Find position with enough ones
                    # Next zero position
                    if last_zero_idx + 1 < m:
                        next_zero = zero_pos[last_zero_idx + 1]
                    else:
                        next_zero = n
                    
                    # Ones available after last_zero_pos
                    ones_available = next_zero - last_zero_pos - 1
                    
                    if ones_available >= needed:
                        # Can satisfy the condition
                        # First valid position is last_zero_pos + needed
                        first_valid = last_zero_pos + needed
                        result += next_zero - first_valid
        
        return result