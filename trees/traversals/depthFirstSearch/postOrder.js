export default class postOrderTraverse{

    constructor(){
        this.arr =[]
    }

    traverse(node){
        const traverseRecursive = (node) => {
            if(node.left!=null){
                traverseRecursive(node.left)
            }
            if(node.right !=null){
                traverseRecursive(node.right)
            }
            this.arr.push(node.value)
        }
        traverseRecursive(node)
        return this.arr
    }
}