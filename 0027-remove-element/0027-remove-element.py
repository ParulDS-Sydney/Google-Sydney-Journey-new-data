class Solution(object):
    def removeElement(self, nums, val):
        # 'i' hamara slow pointer hai jo 'good' numbers ki position track karega
        i = 0
        
        # 'j' hamara fast pointer hai jo poori list ko scan karega
        for j in range(len(nums)):
            # Agar current number target 'val' ke barabar NAHI hai
            if nums[j] != val:
                # Is number ko slow pointer wali jagah par bitha dein
                nums[i] = nums[j]
                # Slow pointer ko ek kadam aage badhayein
                i += 1
        
        # 'i' hi hamari nayi list ki length hogi
        return i
        