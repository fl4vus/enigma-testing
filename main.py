import string

LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

rsize = len(LETTERS)

def swap(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst
    
def lin_search(character_list, character):
    index = -1
    for i in range(len(character_list)):
        if (character == character_list[i]):
            index = i
            break
    
    return index

def cycle_list(lst):
    for i in range(len(lst) - 1):
        swap(lst, i, i + 1)

class Rotors:
    def __init__(self, num, sec_key, notch):
        self.num = num
        self.primary = list(LETTERS)
        self.secondary = list(str(sec_key).upper())
        self.notch = notch
        if (len(self.secondary) != rsize):
            print("ERROR INITIALIZING ROTORS")
            quit()

class Reflectors:
    def __init__(self, num, sec_key):
        self.num = num
        self.primary = list(LETTERS)
        self.secondary = list(str(sec_key).upper())
        if (len(self.secondary) != rsize):
            print("ERROR INITIALIZING ROTORS")
            quit()
            
class Plugboard:
    def __init__(self, swap_lists):
        self.primary = list(LETTERS)
        self.secondary = list(LETTERS)
        
        if (len(swap_lists) > 0):
            for i in range (len(swap_lists)):
                swap(self.secondary, lin_search(self.secondary, swap_lists[i][0]), lin_search(self.secondary, swap_lists[i][1]))

def assemble(components):
    component_order = []
    
    component_order.append(plugboard)
    
    for i in range(3):
        if (components[i] == 1):
            component_order.append(rotor_i)
        elif (components[i] == 2):
            component_order.append(rotor_ii)
        elif (components[i] == 3):
            component_order.append(rotor_iii)
        elif (components[i] == 4):
            component_order.append(rotor_iv)
        elif (components[i] == 5):
            component_order.append(rotor_v)
    
    if (components[3] == 1):
        component_order.append(reflector_a)
    elif (components[3] == 2):
        component_order.append(reflector_b)
    elif (components[3] == 3):
        component_order.append(reflector_c)
    
    return component_order

rotor_i = Rotors(1, 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
rotor_ii = Rotors(2, 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
rotor_iii = Rotors(3, 'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
rotor_iv = Rotors(4, 'ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J')
rotor_v = Rotors(5, 'VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')

reflector_a = Reflectors(1, 'EJMZALYXVBWFCRQUONTSPIKHGD')
reflector_b = Reflectors(2, 'YRUHQSLDPXNGOKMIEBFZCWVJAT')
reflector_c = Reflectors(3, 'FVPJIAOYEDRZXWGCTKUQSBNMHL')

swap_lists = []
components = [3,1,2,2]
plugboard = Plugboard(swap_lists)

assembled = assemble(components)

print(assembled)

inputs = list("AFV JHNETUI :*".upper())
outputs = []

for i in range (len(inputs)):
    outputs.append('x')

rotations = 0

for i in range(len(inputs)):
    if (lin_search(LETTERS, inputs[i]) != -1):
        rotations += 1

print(rotations)
print(len(inputs))

rot1 = 0
rot2 = 0

for i in range(len(inputs)):
    if (lin_search(LETTERS, inputs[i]) == -1):
        outputs[i] = inputs[i]
        print(inputs[i])
    else:
        if (assembled[1].primary[0] == assembled[1].notch):
            if (assembled[2].primary[0] == assembled[2].notch):
                cycle_list(assembled[3].primary)
                cycle_list(assembled[3].secondary)
                
            cycle_list(assembled[2].primary)
            cycle_list(assembled[2].secondary)
        
        cycle_list(assembled[1].primary)
        cycle_list(assembled[1].secondary)
        
        current_char = inputs[i]
        current_pos = lin_search(assembled[0].secondary, current_char)
        # print(current_char, " ", current_pos)
        
        for j in range(1, len(assembled) - 1, 1):
            current_char = assembled[j].secondary[current_pos]
            current_pos = lin_search(assembled[j].primary, current_char)
           #  print(current_char, " ", current_pos)
        
        # reflection
        '''
        print()
        print("reflection")
        print(assembled[4].secondary)
        '''
        current_char = assembled[4].secondary[current_pos]
        current_pos = lin_search(assembled[4].primary, current_char)
        # print(current_char, " ", current_pos)
        
        # print()
        
        for j in range(len(assembled) - 2, 0, -1):
            '''
            print(assembled[j].primary)
            print(assembled[j].secondary)
            '''
            current_char = assembled[j].primary[current_pos]
            current_pos = lin_search(assembled[j].secondary, current_char)
            # print(current_char, " ", current_pos)
        
        current_char = assembled[0].secondary[current_pos]
        current_pos = lin_search(assembled[0].primary, current_char)
        # print(current_char, " ", current_pos)
        # print()
        
        final_char = current_char
        # print(final_char)
        outputs[i] = final_char
            
final_out = ''.join(outputs)
print(final_out)
   

