class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        source = image[sr][sc]
        rows = len(image)
        columns = len(image[0])
        
        def flood_fill(sr, sc):
            if 0<= sr < rows and 0<= sc < columns and image[sr][sc]==source and image[sr][sc]!= color:
                image[sr][sc] = color
                
                flood_fill(sr-1, sc)
                flood_fill(sr+1, sc)
                flood_fill(sr, sc-1)
                flood_fill(sr, sc+1)
        flood_fill(sr, sc)
        return image