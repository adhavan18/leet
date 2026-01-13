class Solution:
    def separateSquares(self, squares):
        # total area
        total = 0
        for x, y, l in squares:
            total += l * l
        half = total / 2.0

        def area_below(h):
            area = 0.0
            for x, y, l in squares:
                bottom = y
                top = y + l
                if h <= bottom:
                    continue
                elif h >= top:
                    area += l * l
                else:
                    area += (h - bottom) * l
            return area

        # binary search on y
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(60):  # enough for 1e-5 precision
            mid = (low + high) / 2
            if area_below(mid) < half:
                low = mid
            else:
                high = mid

        return low
