total=0

for count in range(1000000):
    count += 1
    if(count % 3 == 0 ): continue
    total += count
    
print(total)