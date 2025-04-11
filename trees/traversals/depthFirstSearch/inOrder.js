export default class inOrderTraverse{
    constructor(){
        this.arr = []
    }

    traverse(node){
        const traverseRecursive = (node) => {
            if(node.left != null){
                traverseRecursive(node.left)
            }
        this.arr.push(node.value)
        if(node.right != null){
            traverseRecursive(node.right)
        }}
        traverseRecursive(node)
        return this.arr
    }
}