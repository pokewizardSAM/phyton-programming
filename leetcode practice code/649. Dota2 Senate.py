class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        players= len(senate)    
        for i in players:
            if senate[i] != senate[-1]:
                senate[-1] = senate[i]
