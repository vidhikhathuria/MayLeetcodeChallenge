# Problem Link: https://leetcode.com/problems/flood-fill/
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def fill(image, sr, sc, previousColor, newColor):
            if (sr < 0 or sr >= len(image) or sc < 0 or
                    sc >= len(image[sr]) or image[sr][sc] != previousColor or
                    image[sr][sc] == newColor):
                return
            image[sr][sc] = newColor
            fill(image, sr + 1, sc, previousColor, newColor)
            fill(image, sr - 1, sc, previousColor, newColor)
            fill(image, sr, sc + 1, previousColor, newColor)
            fill(image, sr, sc - 1, previousColor, newColor)

        fill(image, sr, sc, image[sr][sc], newColor)
        return image

