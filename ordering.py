from googlesearch import search
import wikipedia
global text_queue
global karma
global image_queue
order = order.lower()
print(order)
try :
    
    text_queue[number-1].append(response_dict[order])
    print('correlation found')          
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
            with open(file_path, 'w',encoding="utf-8") as output_file:            
                 response_dict[format_special[1]] = format_special[2]
                 json.dump(response_dict,output_file,ensure_ascii=False)       
        elif format_special[0] == "remove" :
            del response_dict[format_special[1]]
        elif format_special[0] == "edit" :
            with open("D:/insta-groupe-test/ordering.py","w",encoding="utf-8") as file_edit:
                file_edit.write(format_special[1]) 
        elif format_special[0] == "search" :
            query = format_special[1]
            for j in search(query, tld="co.in", num=3, stop=3, pause=2): 
                 text_queue[number-1].append(j)
        elif format_special[0] == "karma":
            text_queue[number-1].append(str(karma))
            print(karma)
        elif format_special[0] == "image" :
            image_queue[number-1].append(format_special[1] + ".jpg")
            print("image command", image_queue )
        elif format_special[0] == "wiki" :
            try : 
                wikipedia.set_lang("fr")
                text_queue[number-1].append(wikipedia.summary(format_special[1],sentences=2))
            except Exception :
                pass
    except Exception :
            print("Bad command identation !! \n Your an asshole")
            pass
else : 
    pass
