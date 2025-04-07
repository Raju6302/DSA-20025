class quickSort{
    sort(arr){
        return this.qSort(arr,0,arr.length-1)
    }

    qSort(arr,low,high){
        if(low<high){
            const pi = this.partition(arr,low,high);

            this.qSort(arr,low,pi-1)
            this.qSort(arr,pi+1,high)
        }
        return arr
    }

    partition(arr,low,high){
        const pivot = arr[low]
        let i=low
        let j=high

        while(i<j){
            while(i<high && arr[i]<=pivot) i++

            while(j>low && pivot<arr[j]) j--

            if(i<j) this.swap(arr,i,j)
        }
        this.swap(arr,low,j)
        return j
    }

    swap(arr,i,j){
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
}
const qs = new quickSort()
const arr = [12,10,9,8,13,5,6]
console.log("Before sorting: " + arr)
sortedArr = qs.sort(arr)
console.log("After sorting: " + sortedArr)
