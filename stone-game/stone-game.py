class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        self.game_stats = dict()
        self.roots = [i for i in range(n, 0, -1) if sqrt(i).is_integer()]
        for i in range(len(self.roots)):
            if self.roots[i] <= n:
                self.f_move = self.roots[i]
                is_win = self.alice_move(n, self.roots[i])
                if is_win:
                    return True
                 
        return False
    
    def bob_move(self, n, move) -> bool:
        n = n - move
        if n == 0:
            return False
        
        for i in range(len(self.roots)):
            if self.roots[i] <= n and n - self.roots[i] >= 0:
                if (n, self.roots[i]) in self.game_stats:
                    if self.game_stats[(n, self.roots[i])]:
                        return self.game_stats[(n, self.roots[i])]
                    continue
                is_win = self.alice_move(n, self.roots[i])
                self.game_stats[(n, self.roots[i])] = is_win
                if is_win:
                    return True
                
        return False
                
    def alice_move(self, n, move) -> bool:
        n = n - move
        if n == 0:
            return True
        
        for i in range(len(self.roots)):
            if self.roots[i] <= n and n - self.roots[i] >= 0:
                is_win = self.bob_move(n, self.roots[i])
                if not is_win:
                    return False
