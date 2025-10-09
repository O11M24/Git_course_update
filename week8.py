

def show_skills(name,*skills )  :

   if skills : 
    print(f"Hello {name} Your Skills Is")
    for s in skills : 
        print(f'- {s}')             
   else : 
      print(f"Hello {name} You Have No Skills To Show")

show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")
