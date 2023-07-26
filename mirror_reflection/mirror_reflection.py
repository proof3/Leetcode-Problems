class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        def reflection(right, distance, factor):

            print(distance, right)
            if distance == 0 and right:
                return 0
            elif distance == p:
                return 1 if right else 2
            elif distance > p:
                return reflection(not right, p - (distance - p), -1)
            elif distance < 0:
                return reflection(not right, -distance, 1)
            else:
                return reflection(not right, distance + q * factor, factor)

        return reflection(True, q , 1)
