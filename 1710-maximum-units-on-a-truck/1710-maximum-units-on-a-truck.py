class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        cap=0
        totUnits=0
        for box,unit in boxTypes:
            totUnits+=unit*min(truckSize-cap,box)
            cap+=min(truckSize-cap,box)
        return totUnits
                