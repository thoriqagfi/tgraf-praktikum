import math

# function to compare two pairs


def compare(p1, p2):
	"""For same values, element with the higher index appear earlier in the 
	sorted array. This is for strictly increasing subsequence. For increasing 
	subsequence, the lower index appears earlier in the sorted array.
	"""
	if p1[0] == p2[0]:
		return p1[1] > p2[1]
	return p1[0] < p2[0]

# Function to build the entire Segment tree, the root of which contains the length of the LIS


def buildTree(tree, pos, low, high, index, value):
    """index is the original index of the current element. If the index is not present 
    in the given range, then simply return. If low == high, then the current position 
    should be updated to the value.
    """
    if index < low or index > high:
        return
    if low == high:
        tree[pos] = value
        return
    mid = (high + low) // 2

    # Check if the tree list needs to be extended
    if 2 * pos + 2 >= len(tree):
        tree.extend([0] * (2 * pos + 2 - len(tree) + 1))

    buildTree(tree, 2 * pos + 1, low, mid, index, value)
    buildTree(tree, 2 * pos + 2, mid + 1, high, index, value)
    tree[pos] = max(tree[2 * pos + 1], tree[2 * pos + 2])


# Function to query the Segment tree and return the value for a given range

def findMax(tree, pos, low, high, start, end):
	"""Query: Same as the query function of Segment tree. If the current range 
	is totally inside the query range, return the value of current position. If 
	it is out of bound, return the minimum which would be 0 in this case. Partial 
	overlap. Call findMax on child nodes recursively and return the maximum of the two.
	"""
	if low >= start and high <= end:
		return tree[pos]
	if start > high or end < low:
		return 0
	mid = (high + low) // 2
	return max(findMax(tree, 2 * pos + 1, low, mid, start, end),
			findMax(tree, 2 * pos + 2, mid + 1, high, start, end))

# Function to find Longest Increasing Sequence 

def findLIS(arr):
	"""The array of pairs stores the integers and indices in p[i]. Sorting 
	the array in increasing order of the elements. Calculating the length of 
	the segment-tree. Initializing the tree with zeroes. Building the segment-tree, 
	the root node of which contains the length of LIS for the n elements.
	"""
	n = len(arr)
	p = [(arr[i], i) for i in range(n)]
	p.sort(key=lambda x: (x[0], -x[1]))
	len_tree = 2 ** (math.ceil(math.sqrt(n)) + 1) - 1
	tree = [0] * len_tree
	for i in range(n):
		buildTree(tree, 0, 0, n - 1, p[i][1],
				findMax(tree, 0, 0, n - 1, 0, p[i][1]) + 1)
	return tree[0]


# Driver code
arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]
print("The array is: " + str(arr))
print("The Length of the LIS is:", findLIS(arr))