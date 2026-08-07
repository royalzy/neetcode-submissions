class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = defaultdict(list)

        for words in strs:
            count = [0] * 26

            for char in words:
                count[ord(char)-ord('a')] += 1

            answer[tuple(count)].append(words)

        return list(answer.values())








        # sets = []
        # answer = []
        # for i in range(len(strs)):
        #     dictionary = {char: strs[i].count(char) for char in sorted(strs[i])}
        #     sets.append(dictionary)
        # unique = [dict(i) for i in {tuple(d.items()) for d in sets}] 

        # for i in unique:
        #     temp = []
        #     for j in range(len(sets)):
        #         if i == sets[j]:
        #             temp.append(strs[j])
        #     answer.append(temp)
        
        # return answer



        # for i in range(len(sets)):
        #     temp = [strs[i]]
        #     for j in range(i+1,(len(sets)),):
        #         if sets[i] == sets[j]:
        #             temp.append(strs[j])
        #     answer.append(temp)
        # return answer


        