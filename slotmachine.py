
<style>
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono');
html{
   display:flex;
   justify-content:center;
   align-items: center;
   width: 100%;
   height: 100%;
   background-image: url('https://source.unsplash.com/collection/327760/1600x900');
   background-size:cover;
}

body{
   width:55%;
   height:60vh;
   border:1px solid lightgray;
   background-color:white;
   border-radius:8px;
   font-family: 'Roboto Mono', monospace;
   box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
   border-top:32px solid #eee;
   overflow-y:scroll;
}

body > div{
  height: calc(100% - 40px);
  overflow-y:auto;
  padding: 20px;
  font-size: 24px;
  white-space: pre;
}

pre{
  margin:inherit;
  font-family: inherit;
}
</style>
#!/usr/bin/python3
print("Content-type: text/html \n")

import magicwand
import random 

item1 = random.randint(0,3)
item2 = random.randint(0,3)
item3 = random.randint(0,3)
item4 = random.randint(0,3)
item5 = random.randint(0,3)
item6 = random.randint(0,3)

things = ["&#127821;","&#127819;","&#127824;","&#127817;"]

print(things[item1], ":", things[item2], ":", things[item3], ":", things[item4], ":", things[item5], ":", things[item6])

def slot_machine(item1,item2,item3):
    if item1 == item2 and item2 == item3 and item3 == item4 and item4 == item5 and item5 == item6:
        return "A dollar"
    elif item1 == item2 or item2 == item3 or item3 == item4 or item4 == item5 or item5 == item6:
        return "A thousand dollars"
    else: 
        return "Nothing"
reward = slot_machine(item1,item2,item3)
print("You win: ", reward) 
