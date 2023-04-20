# Given two lists, write a function to find the common 
# elements between them and return them in a new list.
list1 = [4,5,3,2,6,8,9]
list2 = [3,12,14,5]
common_element = list(set(list1).intersection(list2))
print(common_element)

# Write a function that takes in a list of numbers and 
# returns a new list containing only the prime numbers.
def prime_number(nums):
    x=[]
    for i in nums:
        if i%2==1:

           x.append(i)

    
           return x
    
        
    
y=[2,3,45,77,8]
print(prime_number(y))


# # number = [45,12,18,5,7,55,17,37,10]
# # for num in number
# # Write a program that takes in a list of words and 
# # sorts them based on the number of vowels in each word.
def list_vowels(words):
      x='iuoea'
      for l in words:
          if l in x:
              count =0
              return x.sort()
      
