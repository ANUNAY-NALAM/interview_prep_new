
#high retails the lowest value if low>high
def solve(m,n):
    low =1
    high =m
    while low<=high:
        mid =(low+high)//2
        if (mid**n)==m:
            return mid
        if (mid**n)>m:
            high = mid-1
        if (mid**n)<m:
            low = mid+1
    return high
        
if __name__ == "__main__":
    m= 28
    n=3
    print(solve(m,n))