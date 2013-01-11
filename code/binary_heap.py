# This is a Binary Heap implementation using a Python List as an Array.
# To do: change the display so that it shows levels from bottom to top.
import math

class Binary_Heap:

    def __init__(self, elements=[]):
        self.elements = elements;

    def _swap_(self, index1, index2):
        temp = self.elements[index1]
        self.elements[index1] = self.elements[index2]
        self.elements[index2] = temp
        return
    
    def _sift_up_(self, child):
        parent = (child - 1) / 2
        if child == 0 or self.elements[child] >= self.elements[parent]:
            return
        else:
            self._swap_(parent, child)
            self._sift_up_(parent)
            
    def _sift_down_(self, parent):
        try:
            first = self.elements[2 * parent + 1]           
        except IndexError:
            # there are no children, so we stop
            return
        else:
            try:
                second = self.elements[2 * parent + 2]
            except IndexError:
                # there is only a first child
                if self.elements[parent] > first:
                    self._swap_(parent, 2 * parent + 1)
                    self._sift_down_(2 * parent + 1)
                else:
                    return
            else:
                # there is a first child and a second child
                if first <= second:
                    if self.elements[parent] > first:
                        self._swap_(parent, 2 * parent + 1)
                        self._sift_down_(2 * parent + 1)
                    else:
                        return
                else:
                    if self.elements[parent] > second:
                        self._swap_(parent, 2 * parent + 2)
                        self._sift_down_(2 * parent + 2)
                    else:
                        return
    
    def insert(self, item):
        self.elements.append(item)
        self._sift_up_(len(self.elements)-1)

    def remove(self):
        try:
            next = self.elements.pop(0)
        except IndexError: # couldn't pop, list was empty
            return None
        else:
            try:
                self.elements.insert(0, self.elements.pop())
            except IndexError: # couldn't pop, the list was empty
                pass
            else:
                self._sift_down_(0)
            return next

    def show(self):
        if len(self.elements) == 0:
            print "The heap is empty."
            return
        
        # Attempt to print in a nice upside-down V
        
        #print "Last level starts on index", int(pow(2, math.floor(math.log(len(self.elements), 2)))) - 1
        #level_size = int(pow(2, math.floor(math.log(len(self.elements), 2))))
        #index = level_start = level_size - 1
        #while level_size > 0:
        #    while index < level_start + level_size:
        #        try:
        #            print self.elements[index],
        #        except IndexError:
        #            break
        #        index += 1
        #    print
        #    print ' ' * (level_size / 4)
        #    level_size = int(level_size / 2)
        #    index = level_start = level_size - 1       
        
        index = 0
        level_size = 1
        while index < len(self.elements):
            for i in range(level_size):
                try:
                    print self.elements[index + i],
                except IndexError:
                    break
            print
            index += level_size
            level_size *= 2

        #print self.elements


heap = Binary_Heap()

menu_choice = 1
while menu_choice:

    print "\nBinary Heaps:"
    print "0\tExit"
    print "1\tInsert a Node"
    print "2\tRemove Minimal Node"
    print "3\tDisplay the Heap"

    try:
        menu_choice = int(raw_input("Your choice: "))
    except ValueError:
        menu_choice = 0

    if menu_choice == 1:
        try:
            next = int(raw_input("Insert: "))
        except ValueError:
            print "Invalid value. No action taken."
        else:
            heap.insert(next)
    elif menu_choice == 2:
        print "Removing the Minimal Node. Value:", heap.remove()
    elif menu_choice == 3:
        print "Your Heap:"
        heap.show()
    else:
        menu_choice = 0

print "Thanks for trying out binary heaps!"
