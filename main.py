import 
def Tkinter_list_of_colors(original):
 
  v1 = ""
  v2=[]
  list_of_colors=[] #final version
  
  for item in original:
      if item!=" ":
          v1+=item
  
  for item in v1.split(","):
        v2.append(item)
  
  for item in v2:
      original= ""
      for etem in item:
          if etem !="\n":
              original+=etem
      list_of_colors.append(original)



