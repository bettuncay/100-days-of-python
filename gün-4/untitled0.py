import random
random.randint(1,2)

import untitled1
print(untitled1.my_favorite_number)

real_randomization = random.random()
print(real_randomization)

real_randomization = random.random()*10
print(real_randomization)

random_uniform = random.uniform(0,9)
print(random_uniform)

#Yazı Tura Oyunu

sayi = random.randint(1,2)
if sayi == 1:
    print("heads")
else:
    print("tails")

states_of_america = ["delaware, pennsylvania","new jersey"]
print(states_of_america[-1])

states_of_america.append("Hawaii")
print(states_of_america)

states_of_america.extend(["texas","95"])
print(states_of_america)

#Mini Game- London Russian Roulet => Hesabı kim ödeyecek?
import random
friends = ["şüşü","ayşegül","zeynepç","zeynepi","zehra","betül"]
sansli_kisi = random.randint(0,5)
if sansli_kisi == 0:
    print("şüşü")
elif sansli_kisi == 1:
    print("ayşegül")
elif sansli_kisi == 2:
    print("zeynepç")
elif sansli_kisi == 3:
    print("zeynepi")
elif sansli_kisi == 4:
    print("zehra")
else:
    print("betül")    
##Way-2
random.choice(friends)
##Way-3
random_choice = random.randint(0,5)
print(friends[random_choice])


print(len(states_of_america))


kizlar =["betus","ayse","sena"]
erkekler = ["enes","cengiz","muhammed"]
aile = [kizlar,erkekler]
print(aile)