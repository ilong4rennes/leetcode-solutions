# Last updated: 9/25/2025, 2:26:17 AM
class Solution:
    def romanToInt(self, s: str) -> int:
        
        return (s.count("I") + (5 * s.count("V")) + (10 * s.count("X")) + (50 * s.count("L")) + (100 * s.count("C")) + (
                    500 * s.count("D")) + (1000 * s.count("M")) - (2 * s.count("IV")) - (2 * s.count("IX")) - (
                            20 * s.count("XL")) - (20 * s.count("XC")) - (200 * s.count("CD")) - (200 * s.count("CM")))
