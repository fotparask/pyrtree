class Cuboid:

    def __init__ (self, x_min: float, x_max: float , y_min:float, y_max: float, z_min:float, z_max: float):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max



    #the union perimeter of two rectangles
    def pairedVolume(self, rect):

        x_min1 = min(self.x_min, rect.x_min)
        x_max1 = max(self.x_max, rect.x_max)
        y_min1 = min(self.y_min, rect.y_min)
        y_max1 = max(self.y_max, rect.y_max)
        z_min1 = min(self.z_min, rect.z_min)
        z_max1 = max(self.z_max, rect.z_max)
        
        xVar = abs(x_max1-x_min1)
        yVar = abs(y_max1-y_min1)
        zVar = abs(z_max1-z_min1)


        return xVar * yVar * zVar


    def findEdgedValues(self, edgedVars: list):
        
        min_x = min(self.x_min, edgedVars[0])
        max_x = max(self.x_max, edgedVars[1])
        min_y = min(self.y_min, edgedVars[2])
        max_y = max(self.y_max, edgedVars[3])
        min_z = min(self.z_min, edgedVars[4])
        max_z = max(self.z_max, edgedVars[5])

        return min_x, max_x, min_y, max_y, min_z, max_z


    #function that defines the space needed for the rectangle to expand
    #in order to fit in the new Data entry
    def spaceNeeded(self, rect):
        x_min_diff = abs(self.x_min - rect.x_min)
        x_max_diff = abs(self.x_max - rect.x_max)
        y_mix_diff = abs(self.y_min - rect.y_min)
        y_max_diff = abs(self.y_max - rect.y_max)
        z_mix_diff = abs(self.z_min - rect.z_min)
        z_max_diff = abs(self.z_max - rect.z_max)

        x_diff = x_min_diff + x_max_diff
        y_diff = y_mix_diff + y_max_diff
        z_diff = z_mix_diff + z_max_diff

        return x_diff + y_diff + z_diff


