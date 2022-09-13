class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        
        roomsToVisit=deque([])
        roomsToVisit.append(0)

        n=len(rooms)
        
        
        while roomsToVisit:
            room=roomsToVisit.pop()
            if room in visited:
                continue
            visited.add(room)
            for i in rooms[room]:
                roomsToVisit.append(i)            
        
        return len(roomsToVisit)==0 and len(visited)==n