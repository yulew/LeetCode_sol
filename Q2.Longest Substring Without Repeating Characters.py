class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        store=""
        i=-1
        
        while i<len(s)-1:
            
            store1=""
            while i<len(s)-1:
                i+=1                        
                if s[i] not in store1:
                    store1+=s[i]
                    if i==len(s)-1 and len(store)<=len(store1):
                        #print(store1)
                        return len(store1)
                    
                else:
                    m=store1.index(s[i])#give me the position
                    
                    if len(store)<len(store1):
                        store=store1
                    i=m#minus the position
                    break
            
        return len(store)
