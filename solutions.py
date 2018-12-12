from array import *
from collections import Counter, deque
import timeit
import math
import datetime


########################################################################################################
#ARRAY
########################################################################################################

#How do you find the missing number in a given integer array of 1 to 100?
arr = [1,2,3,4,6,7,8]
def findMissingIterative(arr):
    start = 0
    end = len(arr)-1
    while 1:
        midpoint = (end-start)//2 + start
        if midpoint == start:
            return end + 1 if arr[midpoint] == midpoint+1 else midpoint + 1
        if arr[midpoint] != midpoint + 1:
            end = midpoint
        else:
            start = midpoint

def findMissingRecursive(arr,start,end):
    midpoint = (end-start)//2 + start
    if midpoint == start:
        return end + 1 if arr[midpoint] == midpoint+1 else midpoint + 1
    if arr[midpoint] != midpoint + 1:
        return findMissingRecursive(arr,start,midpoint)
    else:
        return findMissingRecursive(arr,midpoint,end)

#you could also calculate the sum of the array and subtract it from n(n+1)/2
# that gives you linear time and space
# for multiple missing numbers calculate sum of squares, cubes, etc of array and construct equation set.

#How do you find all pairs of an integer array whose sum is equal to a given number? (solution) bonus: linear time
arr = [1,2,3,4,5,6,7,8]
def findSumPairsLinearTime(arr,s):
    candidates = set()
    pairs = []
    for num in arr:
        if num < s:
            if s-num in candidates:
                pairs.append((num,s-num))
            else:
                candidates.add(num)
    return pairs

#How do you remove duplicates from an array in place? (solution)
arr = [1,7,2,3,4,4,4,4,5,6,7,8]
def removeDuplicatesInPlace(arr):
    arr.sort()
    i = 1
    while i < len(arr):
        if arr[i] == arr[i-1]:
            del arr[i]
        else:
            i += 1
    return
removeDuplicatesInPlace(arr)

#find the greatest subset sum of an integer array?
arr = [1,-4,5,6,7,-2,4]
arr = [10,-1,10]
def greatestSubsetSum(arr):
    maxSum = 0
    currSum = 0
    for e in arr:
        currSum = max(e,currSum + e)
        maxSum = max(currSum,maxSum)
    return maxSum

#Write a multiply function that multiples 2 integers without using *
def multiply(x,y):
    return sum([x for i in range(y)])

#Find the most frequent integer in an array
arr = [1,2,2,3,3,3,4,4,4,4]
def mostFrequentInteger_counter(arr):
    c = Counter(arr)
    return c.most_common(1)

def mostFrequentInteger_customDict(arr):
    class d(dict):
        def __missing__(self,k):
            self[k] = 0
            return self[k]
    d = d()
    for e in arr:
        d[e] += 1
    return d

def mostFrequentInteger_fastest(arr):
    arr.sort()
    mostFreq = [0,0]
    curr = [arr[0],1]
    for e in arr[1:]:
        if e == curr[0]:
            curr[1] += 1
        else:
            mostFreq = curr if curr[1] > mostFreq[1] else mostFreq
            curr = [e,1]
    mostFreq = curr if curr[1] > mostFreq[1] else mostFreq
    return mostFreq


#Given 2 integer arrays, determine of the 2nd array is a rotated version of the 1st array. Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}
def is_rotated(l1,l2):
    for i,e in enumerate(l1):
        if e == l2[0]:
            #possible start of rotated array
            done = True
            for i2,e2 in enumerate(l1[i:] + l1[:i]):
                if e2 != l2[i2]:
                    done = False
                    break
            if done:
                return True

#Write fibbonaci iteratively and recursively (bonus: use dynamic programming
def fibonaci_iterative(n):
    if n <= 2:
        return 1
    before_last = 1
    last = 1
    for i in range(2,n):
        fib = last + before_last
        before_last, last = last, fib
    return fib

def fibonaci_recursive(n):
    if n<=2:
        return 1
    return fibonaci_recursive(n-1) + fibonaci_recursive(n-2)

#Find the only element in an array that only occurs once.
def find_only_unique(l):
    l.sort()
    for i,e in enumerate(l):
        if (i + 1 == len(l) or l[i+1] != e) \
            and (i == 0 or l[i-1] != e):
            return e

#Find the common elements of 2 int arrays
def find_common_set(l1,l2):
    return set(l1) & set(l2)

#(O(nlogn))
def find_common(l1,l2):
    l1.sort()
    l2.sort()
    common = set()
    i2 = 0
    for e1 in l1:
        while l2[i2] < e1 and i2 < len(l2) - 1:
            i2 +=1
        if l2[i2] == e1:
            common.add(e1)
    return common

#Write a function that prints out the binary form of an int
def to_binary(i):
    if i == 0:
        return '0'
    msb = math.floor(math.log(i,2))
    binary = ''
    while msb >= 0:
        if i - 2**msb >= 0:
            binary += '1'
            i -= 2**msb
        else:
            binary += '0'
        msb -= 1
    return binary

#Implement parseInt
def parse_int(i):
    if i == 0:
        return '0'
    chars = '0123456789'
    string = ''
    place = math.floor(math.log(i,10))
    while place >= 0:
        d = math.floor(i/10**place)
        string += chars[d]
        i -= d*10**place
        place -= 1
    return string

#Implement an exponent function in log(n) time
def exponent(x,y):
    if y == 0:
        return 1
    if y == 1:
        return x
    i = 2
    result = x * x
    while i*2 <= y:
        result *= result
        i *= 2
    for _ in range(i,y):
        result *= x
    return result


########################################################################################################
#STRING
########################################################################################################

#Check if a String is composed of all unique characters
def isAllUnique(str):
    chars = set()
    for c in str:
        if c in chars:
            return False
        else:
            chars.add(c)
    return True

#How do you check if two strings are anagrams of each other? (solution)
def is_anagram_2(s1,s2):
    return sorted(s1) == sorted(s2)

#How do you print the first non-repeated character from a string? (solution)
def first_not_repeated(s):
    repeated = set()
    once = set()
    for c in s:
        if c in once:
            repeated.add(c)
        else:
            once.add(c)
    for c in s:
        if c not in repeated:
            return c

#How do you reverse words in a given sentence without using any library method? (n)
def reverse_str(s):
    word = ""
    out = ""
    for c in s:
        if c == " ":
            out = ' ' + word + out
            word = ''
        else:
            word += c
    out = word + out
    return out

#How do you check if a given string is a palindrome? (solution)
def is_palindrome(s):
    for i,(start,end) in enumerate(zip(s,s[::-1])):
        if start != end:
            return False
        if i > len(s)/2:
            return True

#determine which football week it is
def get_ff_week(date):
    delta = date - datetime.date(2018,9,4)
    return delta.days//7 + 1

#How can a given string be reversed using recursion?
def recursive_reverse(s):
    if len(s) == 1:
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]

#HARD: Find the longest palindrome in a String
def longest_palindrome(s):
    longest = ""
    for i,c in enumerate(s):
        for j in range(len(s)-1,-1,-1):
            #start palindrome potentially
            half = (j-i+1)//2
            if s[i:i+half] == s[j:j-half:-1]:
                #palindrome found
                if j!=i and len(s[i:j+1]) > len(longest):
                    longest = s[i:j+1]
    return longest


#HARD: Print all permutations of a String
#HARD: Given a single-line text String and a maximum width value, write the function 'String justify(String text, int maxWidth)' that formats the input text using full-justification, i.e., extra spaces on each line are equally distributed between the words; the first word on each line is flushed left and the last word on each line is flushed right
#
#LINKEDLIST
#
#Implement a linked list (with insert and delete functions)

class LinkedList():
    def __init__(self,head):
        self.head = head

class Node():
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next


#Given a circular linked list, find the node at the beginning of the loop. Example: A-->B-->C-->D-->E -->C, C is the node that begins the loop
#Reverse a linked list iteratively and recursively
def reverse_linked_list_recursive(node):
    if node.next is None:
        return node
    else:
        curr = node
        while curr.next is not None:
            curr = curr.next
        curr.next = reverse_linked_list_recursive(node)
        return curr

#How do you find the middle element of a singly linked list in one pass?
##A: iterate through adding nodes to an array, then return middle of array

#How do you find the third node from the end in a singly linked list? (solution)
##A: iterate through, keep track of the last node and the node before the last node

#How do you find the sum of two linked lists using Stack? (solution)
#
#BINARY TREE
#
#Implement a binary tree
class BinaryTree():
    #initialize bst from list of values
    def __init__(self,*args):
        self.val = None
        for arg in args:
            self.insert_bst(arg)

    def __repr__(self):
        return str(self.val)

    #TODO
    #HARD: Construct a BST given the pre-order and in-order traversal Strings
    @staticmethod
    def make_tree(preorder,inorder):
        root = BinaryTree(preorder[0])
        r_i = inorder.index(preorder[0])
        if r_i > 0:
            root.left = BinaryTree.make_tree(preorder[1:r_i+1],inorder[:r_i] )
        if r_i < len(inorder) - 1:
            root.right = BinaryTree.make_tree(preorder[r_i+1:],inorder[r_i+1:])
        return root


    #insert into BST (left node < root < right node)
    def insert_bst(self,val):
        if self.val is None:
            self.val = val
        else:
            if val < self.val:
                if hasattr(self,'left'):
                    self.left.insert_bst(val)
                else:
                    self.left = BinaryTree(val)
                    
            if val > self.val:
                if hasattr(self,'right'):
                    self.right.insert_bst(val)
                else:
                    self.right = BinaryTree(val)

    def find_smallest(self):
        if self.left is not None:
            return find_smallest(self.left)
        else:
            return find_replacement(self.left)

    def find_greatest_predecessor(self):
        if self.left is None:
            return self.right
        else:
            return find_replacement(self.left)

    #TODO
    #delete from BST (left node < root < right node)
    def delete_bst(self, val):
        #find val
        if val < self.val:
            if self.left.val == val:
                replacement = find_replacement(self.left)
                self.left = replacement
                delete_bst(self.left, self)
            else:
                self.left.delete_bst(val, self)
        if val > self.val:
            if self.right.val == val:
                pass
            else:
                self.right.delete_bst(val, self)
        if val == self.val:
            if self.right is not None:
                ls = self.find_lowest_successor(self.right)
                parent
            #find lowest sucessor
            lowest_successor = self.find_lowest_successor()
            val = lowest_successor
            self.right.delete_bst(lowest_successor)

    #print all longest paths (dfS)
    def longest_path(self):
        longest = [self.val]
        if hasattr(self,'left'):
            longest_left = self.left.longest_path()
        else:
            longest_left = []
        if hasattr(self,'right'):
            longest_right = self.right.longest_path()
        else:
            longest_right = []
        longest_child = max(longest_left,longest_right, key=len)
        longest += longest_child
        return longest

    #root, left, right
    def print_preorder_traversal(self):
        pre = [self.val]
        if hasattr(self,"left"):
            pre += self.left.print_preorder_traversal()
        if hasattr(self,"right"):
            pre += self.right.print_preorder_traversal()
        return pre

    #HARD
    def print_preorder_traversal_iterative(self):
        curr = self
        out = [curr.val]
        while hasattr(curr,'left') or hasattr(curr,'right'):
            if hasattr(curr,'left'):
                out.append(curr.left.val)

    #left, root, right
    def print_in_order_traversal(self):
        inorder = []
        if hasattr(self,"left"):
            inorder += self.left.print_in_order_traversal()
        inorder.append(self.val)
        if hasattr(self,"right"):
            inorder += self.right.print_in_order_traversal()
        return inorder

    #left, right, root
    def print_postorder_traversal(self):
        postorder = []
        if hasattr(self,"left"):
            postorder += self.left.print_postorder_traversal()
        if hasattr(self,"right"):
            postorder += self.right.print_postorder_traversal()
        postorder.append(self.val)
        return postorder

    #Print a tree by levels (bfs)
    def print_levels(self):
        levels = []
        q = deque()
        q.append(self)
        while len(q) > 0:
            next = q.popleft()
            if hasattr(next,"left"):
                q.append(next.left)
            if hasattr(next,"right"):
                q.append(next.right)
            levels.append(next.val)
        return levels

    #Write a function that determines if a tree is a BST
    def is_bst(self):
        return (hasattr(self,"left") and self.left.val < self.val and self.left.is_bst or \
                not hasattr(self,"left")) and \
                (hasattr(self,"right") and self.right.val > self.val and self.right.is_bst or \
                not hasattr(self,"right")) 

    #Given a binary tree which is a sum tree (child nodes add to parent), write an algorithm to determine whether the tree is a valid sum tree
    def is_sum_tree(self):
        children = []
        if hasattr(self,'left'):
            children.append(self.left.val)
        if hasattr(self,'right'):
            children.append(self.right.val)
        return  (len(children) == 0 or sum(children) == self.val) and \
                (not hasattr(self,'left') or hasattr(self,'left') and self.left.is_sum_tree()) and \
                (not hasattr(self,'right') or hasattr(self,'right') and self.right.is_sum_tree())

    #TODO
    #HARD: Find the max distance between 2 nodes in a (BST?) tree.
    def find_max_distance(self,n1,n2):
        pass


#
#SORTING
#
#How to implement Iterative QuickSort Algorithm? (solution)
#How to implement Insertion Sort Algorithm? (slution)
#How to implement Merge Sort Algorithm? (solution)
#How to implement Bucket Sort Algorithm? (solution)
#How to implement Counting Sort Algorithm? (solution)
#How to implement Radix Sort Algorithm? (solution)

#Find all subsets of an set recursively
def find_subsets_recursive(l):
    #base
    if len(l) == 1:
        return [l]
    #recursive
    remaining_subsets = find_subsets_recursive(l[1:])
    return [[l[0]]] + remaining_subsets + [rs + [l[0]] for rs in remaining_subsets]

def find_subsets_binary(l):
    # subsets = []
    # for i in range(1,2**len(l)):
    #   byte = format(i,f"0{str(len(l))}b")
    #   subsets.append([l[j] for j,b in enumerate(byte) if b == '1'])
    # return subsets
    return [[ l[j] for j,b in enumerate(format(i,f"0{str(len(l))}b")) if b == '1'] for i in range(1,2**len(l))]


#How to swap two numbers without using the third variable? (solution)
def num_swap_pythonic(x,y):
    x,y = y,x
    return x,y

raster = [[0,0,0,1,1],
          [2,0,0,0,0],
          [2,2,0,0,0],
          [2,2,2,0,0]]
#raster image problem
def closest_distance(raster):
    closest = len(raster) * len(raster[0])
    for y,row in enumerate(raster):
        for x,cell in enumerate(row):
            if cell != 0:
                closest_local = closest
                for y2 in range(y,len(raster)):
                    for x2 in range(x,len(raster[0])):
                        if cell != 0:
                            distance = math.sqrt((y2-y)**2+(x2-x)**2)
                            closest_local = min(distance,closest_local)
                if closest_local < closest:
                    closest = closest_local
                    closest_coor = [(x,y),(x2,y2)]
    return closest, closest_coor

#find islands
map = [[0,0,0,1,1],
      [1,0,0,0,0],
      [1,1,0,0,0],
      [1,1,1,0,0]]
def probe_island(map,y,x,visited):
    visited.add((y,x))
    neighbors = [(y,x+1),(y,x-1),(y+1,x),(y-1,x)]
    for n in neighbors:
        if not 0 <= n.x < len(map[0]) or \
            0 <= n.y < len(map) or \
            map[n.y][n.x] == 0 or \
            n in visited:
            break
        else:
            probe_island(map,n.y,n.x)
def count_islands(map):
    island_count = 0
    visited = set()
    for y,row in enumerate(map):
        for x,cell in row:
            visited.add((y,x))
            if cell == 1:
                island_count += 1
                probe_island(map,y,x,visited)
    return island_count

#binomial search
def find(arr, x, offset=0):
    mid = len(arr)//2
    if arr[mid] == x:
        return offset + mid
    if x > arr[mid]:
        return find(arr[mid+1:],x,mid)
    if x < arr[mid]:
        return find(arr[:mid],x,offset)
    return -1

def find_iterative(arr, x):
    start = 0
    end = len(arr) - 1
    while(start <= end):
        mid = start + (end - start)//2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            start = mid + 1
        elif x < arr[mid]:
            end = mid - 1
    return -1


#find greatest common sequence in 2 arrays
#iterative O(n^2)
def find_longest_sequence_common(a1,a2):
    longest = []
    for i1,e1 in enumerate(a1):
        for i2,e2 in enumerate(a2):
            j1 = i1
            if e1 == e2:
                candidate = []
                while a2[i2] == a1[j1]:
                    candidate.append(a2[i2])
                    j1 += 1
                    i2 += 1
                    if j1 == len(a1) or i2 == len(a2):
                        break
                if len(candidate) > len(longest):
                    longest = candidate
    return longest

#there is a way to do it in O(n) using a suffix tree... see 'Longest common substring problem'
#def find_longest_sequence_suffix_tree(a1,a2):



#HARD: Given a 2D array of 1s and 0s, count the number of "islands of 1s" (e.g. groups of connecting 1s)
#Implement binary search in a rotated array (ex. {5,6,7,8,1,2,3})
#Use dynamic programming to find the first X prime numbers
#Implement squareroot function
#HARD: Given a function rand5() that returns a random int between 0 and 5, implement rand7()
#How to check if two rectangles overlap with each other? (solution)
#How to design a Vending Machine? (solution)
#How to implement an LRU Cache in your favorite programming language? (solution)
#How do you check if a given number is an Armstrong number? (solution)
#How do find all prime factors of a given number? (solution)
#How to find the largest prime factor of a given integral number? (solution)
#Write a Program to print Floyd's triangle? (solution)
#Write a Program to print Pascal's triangle? (solution)
#How to calculate the square root of a given number? (solution)
#How to check if given number is a prime number? (solution)
#How to implement Sieve of Eratosthenes Algorithm? (solution)
#How to add two numbers without using plus operator in Java? (solution)
#Write a Program to subtract two binary numbers? (solution)
#Write a Program to transpose a Matrix? (solution)
#Write a Program to add or subtract two Matrices? (solution)
#Write a Program to multiply two Matrices in Java? (solution)
#Write a Program to find GCD of two numbers using Euclid's Algorithm? (solution)
#How to reverse given Integer in Java? (solution)
#Implement a stack with push and pop functions
#Implement a queue with queue and dequeue functions
#Find the minimum element in a stack in O(1) time
#Write a function that sorts a stack (bonus: sort the stack in place without extra memory)
#Implement a binary min heap. Turn it into a binary max heap
#find all permutations of a set
#HARD: Implement a queue using 2 stacks

##GREEDY ALGORITHMS & SCHEDULING
# Q: Given a list of task start and end times, find an optimal schedule that accomplishes the most tasks
def optimal_schedule(tasks):
    #key is to simply order tasks by which one has next possible earliest end time
    tasks.sort(key=lambda t:t[1],reverse=True)
    sched = [tasks.pop()]
    while len(tasks) > 0:
        next_early_end = tasks.pop()
        if next_early_end[0] > sched[-1][1]:
            sched.append(next_early_end)
    return sched

#given a list of prereq, course pairs, construct all the given course schedules a student can take from start to finish (not necessarily greedy)

##DYNAMIC PROGRAMMING
#Given array of int, find longest sequence of increasing integers
#O(n^2)
def longest_increasing_sequence(arr):
    length = []
    for i, e in enumerate(arr):
        length[i] = 1
        for j, e2 in enumerate(arr[:i]):
            if e2 < e:
                length[i] = max(length[i],length[j] + 1)
    return max(length)
#O(nlogn) solution exists...

#given grid of cells with values, find the path from from the top left corner to the bottom right corner which has the greatest sum, assuming you can only move down and right)
def largest_path_across_grid(grid,start):
    num_rows = len(grid)
    num_cols = len(grid[0])
    start_value = grid[start[1]][start[0]]
    #base case: starting on the cell to the left or above the final cell
    if start == (num_rows-1,num_cols-2) or start == (num_rows-2,num_cols-1):
        return [start_value,grid[-1][-1]]
    else:
        if start[0] == num_cols - 1:
            return [start_value] + largest_path_across_grid(grid,(start[0],start[1]+1))
        if start[1] == num_rows - 1:
            return [start_value] + largest_path_across_grid(grid,(start[0]+1,start[1]))
        else:
            largest_right = largest_path_across_grid(grid,(start[0]+1,start[1]))
            largest_down = largest_path_across_grid(grid,(start[0],start[1]+1))
            if sum(largest_right) > sum(largest_down):
                return [start_value] + largest_right
            else:
                return [start_value] + largest_down

##RANGE QUERY
#given an array, we want to perform many queries where we find the sum of a subarray
#A: construct a sum array once, where each value at position k is the sum of all values at positions <= k. Then the sum of a subarray[a:b] = sumarray[b-1] - sumarray[a-1]. works for multiple dimensions
#For a dynamic array though, you'll need a fenwick tree, or binary index tree. Instead of storing all sums at each point in the array, Construct an array where for each value i, fenwick[i] is equal to the sum of arr[i-k:i], where k is the largest power of 2 that divides i. From then on any subarray sum can be found in log(n) time because any range can be constructed with log(n) additions of values in our fenwick tree (ie sumq(1,7)=sumq(1,4)+sumq(5,6)+sumq(7,7)). See page 88 for a helpful visual. each array element belongs in log(n)

##given an array, we want to perform many queries where we find the minimum of a subarray
#A: construct sparse tree: precalculate minimum of all ranges [a:b] where b-a is a power of 2. Then for a range [x1:x2] where k is the largest power of 2 which doesn't exceed x2-x1, the minimum is equal to min(sparsetree[(x1,x1+k)], sparsetree[x2-k,x2])


def cellCompete(states, days):
    for d in range(days):
        rshift = [0] + states[:-1]
        lshift = states[1:] + [0]
        states = [a^b for a,b in zip(rshift,lshift)]
    return states

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

def generalizedGCD(num, arr):
    return reduce(GCD, arr)

#given list of duration, deadline pairs, find optimal ordering of tasks with the highest score, where score for a task is given by deadline - time task completes
# A: simply order the tasks by duration starting with smallest duration (pg 60 competitive programmers handbook (CPH))
