def get_num_words(text):
    words = text.split()
    return len(words)


lower_count={}
def lower_case(text):
    
    for character in text:
        lower_character= character.lower()
       
        if lower_character in lower_count:
            lower_count[lower_character]+=1
        else:
            lower_count[lower_character]=1
    return lower_count
        
def get_sort_values(item):
         return item["num"]
def sorted(text):
    count_list=[]
    for char, num in text.items():
        count_dict={"char":char, "num":num}
        count_list.append(count_dict)
    count_list.sort(reverse=True, key=get_sort_values)
    return count_list

    