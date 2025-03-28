class bubbleSort{
    constructor(arr){
        this.arr = arr
    }

    sort(){
        for(let i=0;i<this.arr.length-1;i++){
            let swapped=false
            for(let j=0;j<this.arr.length-1-i;j++){
                if(this.arr[j]>this.arr[j+1]){
                    let temp=this.arr[j]
                    this.arr[j]=this.arr[j+1]
                    this.arr[j+1] = temp
                    swapped=true
                }
            }
            if(!swapped) break;
        }
        return this.arr
    }
}

let arr = [4,3,5,1,0,2,6,1]

const bsort = new bubbleSort(arr)

sorted_arr = bsort.sort()

console.log(sorted_arr)