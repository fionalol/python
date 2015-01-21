def counter(start_at=0): 
    count=[start_at] 
    def incr():
        count[0]+=1
        return count[0]
    return incr

count=counter(10)
print count
print count()
print count()
print count()

counter2=counter(20)
print counter2()
print counter2()

print counter(20)
print counter2()

x='*'
lambda x : x*3

x= lambda x : x*3
print type(x)
