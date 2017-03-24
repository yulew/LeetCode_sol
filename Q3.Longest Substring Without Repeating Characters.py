class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        store=""
        store_temp=""
        for i in s:
            if i not in store_temp:
                store_temp+=i
            else:
                ind=store_temp.index(i)
                if len(store_temp)>len(store):
                    store=store_temp
                if ind-len(store_temp)+1!=0:
                    store_temp=""+store_temp[ind-len(store_temp)+1:]+i
                else:
                    store_temp=""+i
        if len(store_temp)>len(store):
            store=store_temp
        return len(store)
