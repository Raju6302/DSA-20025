function mergeSort(arr){
    if(arr.length<=1) return arr
    
    
    const mid = Math.floor(arr.length/2)

    const left = mergeSort(arr.slice(0,mid))
    const right = mergeSort(arr.slice(mid))

    return sortArray(left,right)
}

function sortArray(left,right){
    const combined_array = []
    
    let i=0,j=0;k=0;
    
    while(i<left.length && j<right.length){
        if(left[i]<right[j]){
            combined_array.push(left[i])
            i++
        }
        else{
            combined_array.push(right[j])
            j++
        }
    }

    while(i<left.length){
        combined_array.push(left[i])
        i++
    }
    while(j<right.length){
        combined_array.push(right[j])
        j++
    }
    return combined_array
}

let arr = [12,11,13,5,6,15,14,3,8,9]
sorted_arr = mergeSort(arr)
console.log(sorted_arr)


