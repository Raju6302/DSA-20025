import bFS from "../traversals/breadthFirstSearch/bFS.js";
import inOrderTraverse from "../traversals/depthFirstSearch/inOrder.js";
import preOrderTraverse from "../traversals/depthFirstSearch/preOrder.js";
import postOrderTraverse from "../traversals/depthFirstSearch/postOrder.js";

class Node{
    constructor(value){
        this.value = value;
        this.left = null
        this.right = null
    }
}

class binarySearchTree{
    constructor(){
        this.root = null;
    }

    insert(value){
        function insertRecursive(node,value){
            if(node == null) 
                return new Node(value)
            else if(value<node.value){
                node.left =  insertRecursive(node.left, value)
            }
            else if(value>node.value){
                node.right = insertRecursive(node.right, value)
            }
            return node
        }
        this.root = insertRecursive(this.root,value)
    }
    
    delete(value){
        function deleteRecursive(node,value){
            if(node == null) return null;
            else if(value<node.value){
                node.left = deleteRecursive(node.left,value)
            }
            else if(value>node.value){
                node.right = deleteRecursive(node.right,value)
            }
            else{
                if(node.left==null && node.right==null) return null
                else if(node.left == null) return node.right;
                else if(node.right == null) return node.left;
                
                const minNode = this.findMin(node.right)
    
                node.value = minNode.value
    
                node.right = this.deleteRecursive(node.right,minNode.value)
            }
            return node
        }
        deleteRecursive(this.root,value)
    }
    
    findMin(node){
        while(node.left!=null)
            node = node.left

        return node
    }

    search(value){
        searchRecursive(this.root,value);
    }
    searchRecursive(node,value){
        if(node==null) return null

        if (value<node.value) return this.searchRecursive(node.left,value)
        else if(value>node.value) return this.searchRecursive(node.right,value)
        
        return node

    }

}

const _bfs = new binarySearchTree()

_bfs.insert(47);
_bfs.insert(21);    
_bfs.insert(76);
_bfs.insert(18);
_bfs.insert(27);
_bfs.insert(52);
_bfs.insert(82);

const traversals = new bFS()
console.log(traversals.bfs(_bfs.root))

_bfs.delete(18)

console.log(traversals.bfs(_bfs.root))

const inOrder = new inOrderTraverse()

console.log(inOrder.traverse(_bfs.root))
const preOrder = new preOrderTraverse()

console.log(preOrder.traverse(_bfs.root))
const postOrder = new postOrderTraverse()

console.log(postOrder.traverse(_bfs.root))