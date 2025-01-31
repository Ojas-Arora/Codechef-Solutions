def main():
    JEE = int(input())  

    while JEE > 0:
        
        JEE -= 1
        
        GATE = input().strip()  
        
        Ojas = "ADVITIYA" 
        
        MAGGI = 0  

        for NEET in range(8):
            
            KISS = abs(ord(GATE[NEET]) - ord(Ojas[NEET]))
            
            LOVE = min(KISS, 26 - KISS)  
            
            MAGGI += LOVE

        print(MAGGI)