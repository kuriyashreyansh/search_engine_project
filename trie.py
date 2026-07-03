class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        current_node=self.root
        for i in word:
            if i not in current_node.children:
                current_node.children[i]=TrieNode()
            current_node=current_node.children[i]
        current_node.is_end=True

    def search_prefix(self,prefix):
        prefix_node=self.root
        empty_list=[]
        for i in prefix:
            if i not in prefix_node.children:
                return empty_list
            else:
                prefix_node=prefix_node.children[i]
        self._collect(prefix_node,prefix,empty_list)
        return empty_list

    def _collect(self,node,prefix,results):
        if node.is_end==True:
            results.append(prefix)
        for i in node.children:
            self._collect(node.children[i],prefix+i,results)
        
        return results
    

trie = Trie()
trie.insert("neural")
trie.insert("network")
trie.insert("neuroscience")
trie.insert("machine")

print(trie.search_prefix("neur"))  # should give ["neural", "neuroscience"]
print(trie.search_prefix("net"))   # should give ["network"]  
print(trie.search_prefix("xyz"))   # should give []