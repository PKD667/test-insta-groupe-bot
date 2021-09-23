from googlesearch import search
order = order.lower()
global text_queue
global karma
global image_queue
try :
    print('correlation found')
    text_queue[number-1].append(response_dict[order])          
except Exception :
    pass
if order == "good bot" :
    karma += 1
elif order == "bad bot" :
    karma -= 1
if order[0:1] == "!" :
    try :
        special = order[1:]
        try :
           format_special = special.split(":")
        except Exception :
            pass
        if format_special[0] == "kill" :
            Break = True
        elif format_special[0] == "add" :
            with open(file_path, 'w') as output_file:            
                 response_dict[format_special[1]] = format_special[2]
                 output_file.write(json.dumps(response_dict))       
        elif format_special[0] == "remove" :
            del response_dict[format_special[1]]
        elif format_special[0] == "edit" :
            with open("D:/insta-groupe-test/ordering.py","w") as file_edit:
                file_edit.write(format_special[1]) 
        elif format_special[0] == "search" :
            query = format_special[1]
            for j in search(query, tld="co.in", num=5, stop=5, pause=2): 
                 text_queue[number-1].append(j)
        elif format_special[0] == "karma":
            text_queue[number-1].append(str(karma))
            print(karma)
        elif format_special[0] == "image" :
            image_queue[number-1].append("go")
    except Exception :
            print("Bad command identation !! \n Your an asshole")
            pass
else : 
    pass
