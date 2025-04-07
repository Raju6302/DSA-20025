class insertSort{
    constructor(arr){
        this.arr = arr;
    }
    sort(){
        for(let i=1;i<this.arr.length;i++){
            let j=i;
            while(j>=0 && this.arr[j-1]>this.arr[j]){
                const temp = this.arr[j-1]
                this.arr[j-1] = this.arr[j]
                this.arr[j] = temp
                j--;
            }
        }
        return this.arr
    }
}
const isort = new insertSort([12,11,13,5,6])
sorted = isort.sort()
console.log(sorted)