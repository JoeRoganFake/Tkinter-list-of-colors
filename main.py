from original_list import original

def Tkinter_list_of_colors(o):
  v1 = ""
  v2=[]
  list_of_colors=[] #final version
  
  for item in o:
      if item!=" ":
          v1+=item
  
  for item in v1.split(","):
        v2.append(item)
  
  for item in v2:
      a = ""
      for etem in item:
          if etem !="\n":
              a+=etem
      list_of_colors.append(a)
  return list_of_colors


final_list=Tkinter_list_of_colors(original)





