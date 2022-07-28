
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
import magicwand, random, sys


words_tuple = ("Indeed", 
               "Subtle", 
               "Closure", 
               "Soup", 
               "Ramen")

print("Can you complete the following words:")
print()

for word in words_tuple:
    jumbled_word = ""
    max_index = len(word) - 1
    rand_index = random.randint(0,max_index)
    rand_index2 = random.randint(0, max_index)
    rand_index3 = random.randint(0, max_index)
    rand_index4 = random.randint(0, max_index)
    for char in word:
        if char == word[rand_index] or char == word[rand_index2] or char == word[rand_index3] or char == word[rand_index4]:
            jumbled_word = jumbled_word + "_"
        else:
            jumbled_word = jumbled_word + char 
    print(jumbled_word)
    w_list = list(word)    
    random.shuffle(w_list) 
    scrambled_word = "".join(w_list)
    print("Hint", scrambled_word)
    print()
    
print()    
print()    
print()    
print()    
print()    
print()    
print()    
print()   
print()    
print()    
print()    
print()    
print()    
print()    

for word in words_tuple:
    print(word)
