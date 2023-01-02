d0={'mango':30,'guava':20}
d1={'apple':70,'pinapple':50}
d2={'kiwi':90,'banana':35}
d3={}
for d in (d0,d1,d2):
    d3.update(d)
print(d3)