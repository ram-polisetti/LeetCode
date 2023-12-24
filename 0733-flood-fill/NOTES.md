(if 0<= sr < rows   and 0<= sc < columns )-> making sure that the function calls wont get out of bound
image[sr][sc]==source  -> making sure that the current pixel have the source color
image[sr][sc]!= color -> avoiding any recursive calls