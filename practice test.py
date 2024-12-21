"""with open("story.txt","r")as f:
    while True:
        i=0
        story=f.readline()
        
        if not story:
            break
        i+=1
        m1=story.split(",")[0]
        m2=story.split(",")[1]
        m3=story.split(",")[2]
        print(f"the marks of student {i} in english {m1}")
        print(f"the marks of student {i} in english {m2}")
        print(f"the marks of student {i} in english {m3}")

"""

# function of tell and seek and turncate
# with open("story.txt","r")as f:
#     f.seek(5)
#     story=f.read(5)
#     print(story)


with open("sampel.txt","a")as f:
    f.write("helo jani how are you ?")
    
    f.truncate(5)
    