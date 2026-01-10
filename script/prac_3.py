in_str = [1,2,3,4,5,6,7]
out_str = list(map(lambda x:x*x , in_str))
print(out_str)
fil_str = list(filter(lambda x:x%2 == 0,in_str))
print(fil_str)