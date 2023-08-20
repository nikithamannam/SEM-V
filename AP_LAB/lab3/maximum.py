def maximum(*numbers):
    if len(numbers)==0:
        return None
    else:
        maxnum=numbers[0]
        for n in numbers[1:]:
            if n>maxnum:
                  maxnum=n

        return maxnum    
