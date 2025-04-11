class insertSort{
    constructor(arr){
        this.arr = arr;
    }
    sort(){
        for(let i=1;i<this.arr.length;i++){
            let key = this.arr[i]
            let j;
            for(j=i-1;j>=0 && this.arr[j]>key;j--){
                this.arr[j+1] = this.arr[j]
            }
            this.arr[j+1] = key;
        }
        return this.arr
    }
}
const isort = new insertSort([12,11,13,5,6])
sorted = isort.sort()
console.log(sorted)