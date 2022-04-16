class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        print("-> Linked List constructed...")
        self.head = None
        self.length = 0

    def __del__(self):
        print("instance deleted...")

    # add first 앞쪽에 넣기
    def addFirst(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    # add last 뒤쪽에 넣기
    def append(self, data):
        cur = self.head
        # 비어있는 경우
        if cur == None:
            self.addFirst(data)
            return
        # 추가하는 경우
        newNode = Node()
        newNode.data = data

        while cur.next != None:
            cur = cur.next
        cur.next = newNode
        self.length += 1
        print("- append suceeded!")


    def showList(self):
        print('*instance ID show list', self)
        print("[", end='')
        node = self.head
        while node:
            print(node.data, end=', ')
            node = node.next
        print("]")
        print('*list length:', self.length)

    # index 값으로 삭제
    def deleteNode(self, index):
        prev = None
        cur = self.head
        index -= 1
        i = 0
        while cur.next != None and i < index:
            prev = cur
            print(cur.data, index)
            cur = cur.next
            i += 1
        if index == i:
            self.length -= 1
            if prev == None:
                self.head = cur.next
            else:
                prev.next = cur.next
        else:
            print('index out of range...')
    def searchByKey(self, key):
        index = 0
        cur = self.head
        while cur != None:
            if cur.data == key:
                print("found match! [", key, "] at index: ", index)
                return
            cur = cur.next
            index += 1
        print('*no match key : ',key)
def main():
    print('[파이썬 링크드 리스트 구현]')
    print('1. 노드생성')
    myLList = LinkedList()
    myLList.append(999)
    myLList.addFirst(1)
    myLList.addFirst(2)
    myLList.addFirst(3)
    myLList.addFirst(4)
    myLList.showList()
    myLList.append(5)
    myLList.append(6)
    myLList.append(7)
    myLList.showList()
    myLList.deleteNode(1)
    myLList.deleteNode(1)
    myLList.deleteNode(1)
    myLList.showList()
    myLList.searchByKey(7)
    listA = "양양이"
    newList = LinkedList()
    newList.append(listA)
    newList.showList()
if __name__ == '__main__':
    main()