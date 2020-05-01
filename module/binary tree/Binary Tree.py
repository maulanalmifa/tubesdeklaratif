# isTree(nil).
# isTree(t(_,nil,nil)):- !.
# isTree(t(_,L,nil)):- isTree(L).
# isTree(t(_,nil,R)):- isTree(R).
# isTree(t(_,L,R)):- isTree(L), isTree(R), !.
def BinarySearch(list1,key) :
	low = 0
	high = len(list1)-1
	Found = False
	while low<= high and not Found:
		mid= (low+high)//2
		if key == list1[mid]:
			Found = True
		elif key>list1[mid]:
			low = mid+1
		else:
			high = mid-1
	if Found == True:
		print("key is Founf")
	else:
		print("key is not Found")

list1 = [23,1,4,2,3]
list1.sort()
print(list1)
