class Node{
    constructor(value){
        this.value = value;
        this.left = null
        this.right = null
    }
}

export default class bFS{
    constructor(){
        this.root = null
    }
    insert(value){
        function insertRecursive(node,value){
            if (node==null) return new Node(value)

            if(value<node.value){
                node.left = insertRecursive(node.left,value)
            }else if(value>node.value){
                node.right = insertRecursive(node.right,value)
            }
            return node
        };
        this.root = insertRecursive(this.root,value)
    }
    bfs(root){
        let result = []
        let queue = []
        queue.push(root)
        while(queue.length>0){
            let currentNode = queue.shift()
            result.push(currentNode.value)
            if(currentNode.left != null) queue.push(currentNode.left)
            if(currentNode.right != null) queue.push(currentNode.right)
        }

        return result

    }
}


const _bfs = new bFS()

_bfs.insert(47);
_bfs.insert(21);    
_bfs.insert(76);
_bfs.insert(18);
_bfs.insert(27);
_bfs.insert(52);
_bfs.insert(82);

console.log(_bfs.root)

console.log(_bfs.bfs(_bfs.root))