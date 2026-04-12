class Solution(object):
    def candy(self, ratings):
        result_list_1 = []
        result_list_2 = []
        result_list_2.append(1)
        result_list_1.append(1)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                result_list_1.append(result_list_1[-1] + 1)
            else:
                result_list_1.append(1)
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                result_list_2.append(result_list_2[-1]+1)
            else:
                result_list_2.append(1)
        min_candy = 0
        for i in range(len(ratings)):
            min_candy  = min_candy + max(result_list_1[i], result_list_2[len(ratings)-1-i])
        return min_candy
        

