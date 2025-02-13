"""
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
 

Constraints:

0 <= val <= 109
At most 2 * 104 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.

"""

from collections import defaultdict

class FreqStack(object):

    def __init__(self):
        self.freq = defaultdict(int)  # Stores frequency of each number
        self.group = defaultdict(list)  # Maps frequency to stack of numbers
        self.max_freq = 0  # Tracks the highest frequency

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] += 1  # Increase frequency of val
        f = self.freq[val]  # Current frequency of val
        
        self.group[f].append(val)  # Add val to its frequency group stack
        self.max_freq = max(self.max_freq, f)  # Update max frequency

    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.max_freq].pop()  # Get most frequent element
        self.freq[val] -= 1  # Reduce frequency count

        if not self.group[self.max_freq]:  # If no elements left at max frequency
            self.max_freq -= 1  # Reduce max frequency
        
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()