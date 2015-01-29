def bubble_sort(arr) 
    sorted = false 
    until sorted do 
        sorted = true 
        
        idx = 0 
        while idx < (arr.count - 1) do 
            if arr[idx] > arr[idx + 1] 
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                sorted = false 
                idx += 1
            end 
            idx += 1
        end 
    end 
    
    return arr
end 