export default class preOrderTraverse{
    constructor(){
        this.arr =[]
    }

    traverse(node){
         const traverseRecursive = (node) => {
            this.arr.push(node.value)

            if(node.left!=null){
                traverseRecursive(node.left)
            }
            if(node.right!=null){
                traverseRecursive(node.right)
            }
         }
         traverseRecursive(node)
         return this.arr
    }

}