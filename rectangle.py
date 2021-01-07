class Rectangle:

    def __init__ (self, x_min: float, x_max: float , y_min:float, y_max: float):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max



    #returns the width of the rectangle
    def rect_x(self):
        return self.x_max - self.x_min



    #returns the height of the rectangle
    def rect_y(self):
        return self.y_max - self.y_min



    #returns the perimeter
    def perimeter(self) -> float:
        return 2 * (self.rect_x + self.rect_y)


    #the union perimeter of two rectangles
    def pairedPerimeter(self, rect: Rectangle):

        x_min1 = min(self.x_min, rect.x_min)
        x_max1 = max(self.x_max, rect.x_max)
        y_min1 = min(self.y_min, rect.y_min)
        y_max1 = max(self.y_max, rect.y_max)
        
        return 2 * ((x_max1 - x_min1) + (y_max1 - y_min1))
        


    def isRectSmallerThan(self, rect: Rectangle):
        if self.x_max < rect.x_min:
            return True
        elif self.x_max < rect.x_min:
            return False
        else:
            if self.y_max < rect.y_max:
                return True
            else:
                return False



    def findEdgedValues(self, edgedVars: list):
        
        min_x = min(self.x_min, edgedVars[0])
        max_x = max(self.x_max, edgedVars[1])
        min_y = min(self.y_min, edgedVars[2])
        max_y = max(self.y_max, edgedVars[3])

        return min_x, max_x, min_y, max_y



    #returns the area the rectangle covers
    def area(self) -> float:
        return self.rect_x * self.rect_y



    #function that defines the space needed for the rectangle to expand
    #in order to fit in the new Data entry
    def spaceNeeded(self, rect: Rectangle):
        x_min_diff = abs(self.x_min - rect.x_min)
        x_max_diff = abs(self.x_max - rect.x_max)
        y_mix_diff = abs(self.y_min - rect.y_min)
        y_max_diff = abs(self.y_max - rect.y_max)

        x_diff = x_min_diff + x_max_diff
        y_diff = y_mix_diff + y_max_diff

        return x_diff + y_diff