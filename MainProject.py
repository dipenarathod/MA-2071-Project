import numpy as np

'''Arrays used for encryption and decryption'''
A=np.array([[2,1],#matrix used for encryption
            [1,0]])
B=np.array([[0,1],#matrix used for decryption(inverse of A modulo 26)
            [1, 24]])


'''Dictionaries used to create pairs'''
mapping={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':0}
reverse_mapping={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',0:'Z'}

unencrypted_message="SENDMOREHOTCHEETOSANDSPICYNACHODORITOS"#Message to be encrypted
unencrypted_message=unencrypted_message.replace(" ","")#Remove blank spaces
if(len(unencrypted_message)%2!=0):#If there are odd number of letters, add the last letter
    unencrypted_message+=unencrypted_message[-1]
print("Original message:")
print(unencrypted_message)



'''Get letter pairs'''
j=0#used as boundary for pairs
unencrypted_message_letter_pairs=[]#matrix to store pairs of letters
for i in range(len(unencrypted_message)//2):
    unencrypted_message_letter_pairs.append(unencrypted_message[j:j+2])#get pairs of letters out
    #print(unencrypted_message_letter_pairs[i])
    j+=2
print("Unencrypted message letter pairs")
print(unencrypted_message_letter_pairs)



'''Get corresponding number pairs'''
unencrypted_message_number_pairs=[]#matrix to store corresponding number pairs present in message_matrix
for i in unencrypted_message_letter_pairs:
    temp_matrix=[]
    for j in i:
        temp_matrix.append([mapping[j]])#.append(mapping[j]) will add the elements to the same row .append([mapping[j]]) will add the elements as different rows
    unencrypted_message_number_pairs.append(temp_matrix)
print("Unencrypted message number pairs")
print(unencrypted_message_number_pairs)



'''Encrypt the number pairs'''
print("Encrypted message number pairs")
encrypted_message_number_pairs=[]#store new pairs after multiplying them with A, and applying modulo 26 to them
for i in unencrypted_message_number_pairs:
    encrypted_message_number_pairs.append(np.matmul(A,i)%26)
    print(np.matmul(A,i)%26)



'''Convert encrypted number pairs to encrypted letter pairs and encrypted message'''
encrypted_message_number_pairs=np.array(encrypted_message_number_pairs)#matrix to store the letters corresponding to the encrypted matrix pairs
encrypted_message_letter_pairs=[]#store pairs of letters of encrypted message in a matrix
encrypted_message=""#store the message in a string form
for i in range(len(encrypted_message_number_pairs)):
    pair=""
    for j in range(len(encrypted_message_number_pairs[i])):
        pair+=reverse_mapping[int(encrypted_message_number_pairs[i][j])]
    encrypted_message_letter_pairs.append(pair)
    encrypted_message+=pair
print("Encrypted message letter pairs")
print(encrypted_message_letter_pairs)
print("Encrypted message")
print(encrypted_message)

#Decryption------------------------------------------------------------------------------------------------------------------

'''Message to be decrypted'''
new_encrypted_message="QSFNOMOREHQTUHDEWOPAADOPECCNNCHOVOLIWO"
print("Message to decrypt")
print(new_encrypted_message)



'''Encrypted letter pairs'''
new_encrypted_message_letter_pairs=[]
k=0
for i in range(len(new_encrypted_message)//2):
    new_encrypted_message_letter_pairs.append(new_encrypted_message[k:k+2])#get pairs of letters out
    #print(new_encrypted_message_letter_pairs[i])
    k+=2
print("Encrypted letter pairs")
print(new_encrypted_message_letter_pairs)



'''Encrypted number pairs'''
new_encrypted_message_number_pairs=[]
for i in new_encrypted_message_letter_pairs:
    temp_matrix=[]
    for j in i:
        temp_matrix.append([mapping[j]])#.append(mapping[j]) will add the elements to the same row .append([mapping[j]]) will add the elements as different rows
    new_encrypted_message_number_pairs.append(temp_matrix)
print("Corresponding encrypted number pairs")
print(new_encrypted_message_number_pairs)



'''Decrypted message number pairs'''
decrypted_message_number_pairs=[]#store new pairs after multiplying them with B, and applying modulo 26 to them
print("Decrypted message number pairs")
for i in new_encrypted_message_number_pairs:
    decrypted_message_number_pairs.append(np.matmul(B,i)%26)#matmul=matrix multiplication, I thought numpy just multiplied matrices when used with the * operator
    print(np.matmul(B,i)%26)
decrypted_message_number_pairs=np.array(decrypted_message_number_pairs)



'''Decrypted message letter pairs and complete message'''
decrypted_message_letter_pairs=[]#store pairs of letters of encrypted message in a matrix
decrypted_message=""#store the message in a string form
for i in range(len(decrypted_message_number_pairs)):
    pair=""
    for j in range(len(decrypted_message_number_pairs[i])):
        pair+=reverse_mapping[int(decrypted_message_number_pairs[i][j])]
    decrypted_message_letter_pairs.append(pair)
    decrypted_message+=pair
print("Decrypted message letter pairs")
print(decrypted_message_letter_pairs)
print("Decrypted message")
print(decrypted_message)

