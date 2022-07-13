def count_substring(string, sub_string):
    n=len(string)#lenght of string 
    m=len(sub_string)#length of sub_string
    #auxiliar variables
    auxN=0
    auxM=0
    count=0
    while(auxN<n):#while loop to travel trough the whole string
        if(string[auxN]==sub_string[auxM]):#conditional for when theres a coincidence in characters
            auxM+=1
            if(auxM==m):##if the whole substring belongs to the string
                count+=1
                auxN-=auxM-1#returns len(sub_string) positions just so search for more appeareances of the substring
                auxM=0
                
        else:#in case string a substring have a different character
            auxM=0    
        auxN+=1   
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)