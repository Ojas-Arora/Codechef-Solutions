def min_sessions(S, inputs):
    outputs = []

    
    for i in range(S):
        P, Q, R = inputs[i]
     
        
        if R >= Q:
            outputs.append(0)
            continue
    
        
        found_solution = False
        for k in range(101):
            discount = k * P
            
            
            if discount > 100:
                discount = 100
           
            
            reduced_price = Q * (100 - discount) / 100
            budget_left = R - k
            
            
            if budget_left >= reduced_price:
                outputs.append(k)
                found_solution = True
                break
        
        if not found_solution:
            outputs.append(-1)
    
    return outputs


S = int(input())
inputs = [tuple(map(int, input().split())) for _ in range(S)]

results = min_sessions(S, inputs)

for output in results:
    print(output)
