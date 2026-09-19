class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest point on the rectangle to the circle's center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate the distance between the closest point and the circle center
        distance_x = xCenter - closest_x
        distance_y = yCenter - closest_y
        
        # Check if the distance is less than or equal to the radius
        return (distance_x ** 2 + distance_y ** 2) <= (radius ** 2)