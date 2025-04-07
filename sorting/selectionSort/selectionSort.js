class selectionSort{
    constructor(arr){
        this.arr = arr
    }

    sort(){
        for(let i=0;i<this.arr.length-1;i++){
            let minIndex = i;
            for(let j=i+1;j<this.arr.length;j++){
                if(this.arr[minIndex] > this.arr[j] ){
                    minIndex = j
                }
            }
            if(minIndex!=i){
                [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
            }
        }
        return this.arr
    }
}
arr=[12,9,8,10,5,6,2,13]
const sSort = new selectionSort(arr)
console.log("Before Sorting: "+ arr)
sortedArr=sSort.sort()
console.log("After Sorting: " + sortedArr)