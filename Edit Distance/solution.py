class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

	#the @cache directive can be used instead of using the solutions dict for memoization
        def tryOp(word1, word2, solutions):
            
            if len(word1) <= 0 and len(word2) > 0 or len(word1) > 0 and len(word2) == 0:
                return max(len(word1), len(word2))
            if len(word1) == 0 and len(word2) == 0:
                return 0

            if word1[0] == word2[0]:
                return tryOp(word1[1:], word2[1:], solutions)
            if (len(word1), len(word2)) in solutions:
                return solutions[(len(word1), len(word2))]

            delt = tryOp(word1[1:], word2,solutions)
            appn = tryOp(word1, word2[1:], solutions)
            repl = tryOp(word1[1:], word2[1:], solutions)
            solutions[(len(word1), len(word2))] = min(delt + 1, appn + 1, repl + 1)
            return (min(delt + 1, appn + 1, repl + 1))

        solutions = dict()
        return tryOp(word1, word2, solutions)
